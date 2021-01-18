#!/usr/bin/env python

import argparse
from pathlib import Path
import json
from multiprocessing import Pool

from pycorenlp import StanfordCoreNLP
from nltk.tree import Tree

import mrt.e2e.mr_utils
import mrt.e2e.rules
import mrt.viggo.mr_utils
import mrt.viggo.rules


def get_rule_set(rule_set):
    if rule_set == "E2E":
        mr_utils = mrt.e2e.mr_utils
        rules = mrt.e2e.rules
    elif rule_set == 'Viggo':
        mr_utils = mrt.viggo.mr_utils
        rules = mrt.viggo.rules
    else:
        raise Exception(f'Bad rule set: {rule_set}')
    return mr_utils, rules
 
def input_iter(path, port, rule_set, freq_info):
    with path.open('r') as fp:
        for line in fp:
            yield line, port, rule_set, freq_info

def phrase_iter(tree):
    for child in tree:
        if isinstance(child, Tree):
            for grandchild in phrase_iter(child):
                yield grandchild
            if child.label() in ["NP", "VP", "ADJP", "ADVP", "PP", "S",
                                 "SBAR"]:
                yield child

def process_example(args):
    line, port, rule_set, freq_info = args
    mr_utils, rules = get_rule_set(rule_set)
    ex = json.loads(line)
    corenlp = StanfordCoreNLP(f'http://localhost:{port}')
    mr = ex['source']['mr']

    # Correct for duplicate names in E2E
    if '|' in mr['slots'].get('name', 'N/A'):
        new_name = mr['slots']['name'].split("|")[0]
        mr['slots']['name'] = new_name
    if '|' in mr['slots'].get('near', 'N/A'):
        new_near = mr['slots']['near'].split("|")[0]
        mr['slots']['near'] = new_near

    ref_string = ex['target']['reference']
    tokens = mr_utils.tokenize(ref_string)
    tokens_delex = mr_utils.delexicalize_tokens(tokens, no_dates=True)
    ref_string_delex = mr_utils.detokenize(tokens_delex)

    new_data = []

    output = corenlp.annotate(
        ref_string_delex,
        properties={'annotators': 'parse,lemma', 'outputFormat': 'json'})
    
    if 'sentences' not in output:
        
        print("===============\n\n" + str(ref_string_delex) + "\n\n" + str(output) + "\n\n")
    for sent in output['sentences']:
        parse_tree_str = sent["parse"]
        tree = Tree.fromstring(parse_tree_str)
        for phrase in phrase_iter(tree):
            
            tokens = phrase.leaves()
            tokens = [t.replace('-LRB-', '(').replace('-RRB-', ')')\
                        .replace('Ltd.', 'Ltd')
                      for t in tokens]

            ws_tokens = ' '.join(tokens).replace('10 +', '10+').split(' ')
            ws_tokens = mr_utils.delexicalize_tokens(ws_tokens, **mr['slots'])
            ws_tokens = mr_utils.tokenize(' '.join(ws_tokens))

            tags = rules.tag_tokens(ws_tokens)
            linear_mr_delex = mr_utils.tags2linear_mr(tags)
            tokens_delex = [x if mr_utils.is_placeholder(x) else x.lower()  
                            for x in ws_tokens]
            reference_delex = mr_utils.detokenize(tokens_delex)
            reference_lex = mr_utils.lexicalize_string(
                reference_delex, **mr['slots'])
            tokens_lex = [x.lower() for x in mr_utils.tokenize(reference_lex)]
            
            linear_mr_lex = mr_utils.lexicalize_linear_mr(
                linear_mr_delex, **mr['slots'])
            if len(linear_mr_delex) == 0:
                continue
            
            #TODO TEST That this is ok
            if any([x.endswith("PLACEHOLDER") for x in linear_mr_lex]):
                continue

            phrase_mr = mr_utils.linear_mr2mr(linear_mr_lex)
            phrase_mr['da'] = mr['da']
            if 'rating' in mr['slots']:
                phrase_mr['slots']['rating'] = mr['slots']['rating']
            linear_mr_delex = mr_utils.mr2header(phrase_mr) + linear_mr_delex
            linear_mr_lex = mr_utils.mr2header(phrase_mr) + linear_mr_lex
            inc_freq_fixed_delex = mr_utils.linearize_mr(
                phrase_mr, delex=True,
                order='inc_freq_fixed',
                freq_info=freq_info)
            inc_freq_fixed_lex = mr_utils.linearize_mr(
                phrase_mr, delex=False,
                order='inc_freq_fixed',
                freq_info=freq_info)
            inc_freq_delex = mr_utils.linearize_mr(
                phrase_mr, delex=True,
                order='inc_freq',
                freq_info=freq_info)
            inc_freq_lex = mr_utils.linearize_mr(
                phrase_mr, delex=False,
                order='inc_freq',
                freq_info=freq_info)

            dec_freq_delex = mr_utils.linearize_mr(
                phrase_mr, delex=True,
                order='dec_freq',
                freq_info=freq_info)
            dec_freq_lex = mr_utils.linearize_mr(
                phrase_mr, delex=False,
                order='dec_freq',
                freq_info=freq_info)

            dec_freq_fixed_delex = mr_utils.linearize_mr(
                phrase_mr, delex=True,
                order='dec_freq_fixed',
                freq_info=freq_info)
            dec_freq_fixed_lex = mr_utils.linearize_mr(
                phrase_mr, delex=False,
                order='dec_freq_fixed',
                freq_info=freq_info)

            phrase_ex = {
                'source': {
                    'phrase': phrase.label(),
                    'mr': phrase_mr,
                    'sequence': {
                        'dec_freq_lex': dec_freq_lex,
                        'dec_freq_delex': dec_freq_delex,
                        'inc_freq_lex': inc_freq_lex,
                        'inc_freq_delex': inc_freq_delex,
                        'inc_freq_fixed_lex': inc_freq_fixed_lex,
                        'inc_freq_fixed_delex': inc_freq_fixed_delex,
                        'dec_freq_fixed_lex': dec_freq_fixed_lex,
                        'dec_freq_fixed_delex': dec_freq_fixed_delex,
                        'rule_lex': linear_mr_lex,
                        'rule_delex': linear_mr_delex,
                    },
                },
                'target': {
                    'sequence': {
                        'lex': tokens_lex,
                        'delex': tokens_delex,
                    },
                    'reference': reference_lex,
                },
            }

            new_data.append(json.dumps(phrase_ex))
    return new_data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("rule_set", choices=['Viggo', 'E2E'])
    parser.add_argument("freqs", type=Path)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--port", default=9000, type=int)
    parser.add_argument("--procs", default=4, type=int)
    args = parser.parse_args()
    args.output.parent.mkdir(exist_ok=True, parents=True)

    freq_info = json.loads(args.freqs.read_text())
    pool = Pool(args.procs)

    with args.output.open('w') as fp:    
        
        in_data = input_iter(args.input, args.port, args.rule_set, freq_info)
        for i, out_data in enumerate(pool.imap(process_example, in_data)):
            print(i, end='\r', flush=True)
            for line in out_data:
                print(line, file=fp)
    print()

if __name__ == '__main__':
    main()
