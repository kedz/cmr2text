#!/usr/bin/env python

import argparse
from pathlib import Path
import csv
import json

import mrt.e2e.mr_utils 
import mrt.e2e.rules 
import mrt.viggo.mr_utils
import mrt.viggo.rules 


def input_iter(path, rule_set, use_corrected, e2e_og):
    with path.open('r') as fp:
        reader = csv.reader(fp)
        next(reader)
        for exid, item in enumerate(reader):
            if not e2e_og:
                mr, text = item[:2]
            else:
                mr, text = item[3], item[1]
            yield [exid, mr, text] + [rule_set, use_corrected]

def format_example(args):
    exid, mr_line, utt_line, rule_set, use_corrected = args
    if rule_set == 'Viggo':
        mr_utils = mrt.viggo.mr_utils
        rules = mrt.viggo.rules

        def add_header(linear_mr, mr):
            header = [mr['da'], f"rating={mr['slots'].get('rating', 'N/A')}"]
            return header + linear_mr

    elif rule_set == 'E2E':
        mr_utils = mrt.e2e.mr_utils
        rules = mrt.e2e.rules

        def add_header(linear_mr, mr):
            return linear_mr
    else:
        raise Exception(f'Bad rule set: {rule_set}')

    # Get the reference string (for BLEU/ROUGE/etc. evals).
    ref = mr_utils.correct_utterance(utt_line)
    # Get dict MR representation. 
    mr = mr_utils.extract_mr(mr_line)

    # Tokenize reference for target sequence with and without delexicalization.
    tokens_lex = mr_utils.tokenize(ref.lower())
    tokens_delex = mr_utils.delexicalize_tokens(tokens_lex, **mr['slots'])

    # Tag lexicalized and delexicalized token sequences. 
    tags_lex = rules.tag_tokens(tokens_lex, **mr['slots'])
    tags_delex = rules.tag_tokens(tokens_delex, **mr['slots'])

    # Get linearized MR from tag sequence. 
    linear_mr_lex = mr_utils.tags2linear_mr(tags_lex)
    linear_mr_delex = mr_utils.tags2linear_mr(tags_delex)

    if not use_corrected:
        orig_lin_mr = mr_utils.linearize_mr(mr)
        orig_lin_mr_delex = mr_utils.linearize_mr(mr, delex=True)
        linear_mr_lex = [x for x in linear_mr_lex if x in orig_lin_mr]
        linear_mr_delex = [x for x in linear_mr_delex 
                           if x in orig_lin_mr_delex]

    example = {
        'orig': {
            'mr': mr,
            'utt': utt_line,
        },
        'source': {
            'sequence': {
                'rule_lex': add_header(linear_mr_lex, mr),
                'rule_delex': add_header(linear_mr_delex, mr),
            },
        },
        'target': {
            'sequence': {
                'lex': tokens_lex,
                'delex': tokens_delex,
            },
            'reference': ref if use_corrected else utt_line,
        },
    }

    return exid, json.dumps(example)

def format_partition(input_path, output_path, rule_set, use_corrected, nprocs,
                     e2e_og):

    from multiprocessing import Pool

    pool = Pool(nprocs)
    chunk_size = 1000 if rule_set == 'E2E' else 1
    input_data = input_iter(input_path, rule_set, use_corrected, e2e_og)
    last_exid = -1
    with output_path.open('w') as out_fp:
        for exid, ex_str in pool.imap(format_example, input_data):
            print(f'{exid}', end='\r', flush=True)
            last_exid += 1 
            assert last_exid == exid
            print(ex_str, file=out_fp)
        print()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('rule_set', choices=['Viggo', 'E2E'])
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument('--test', action='store_true')
    parser.add_argument('--e2e-og', action='store_true')
    parser.add_argument('--procs', default=4, type=int)
    args = parser.parse_args()

    if args.test:
        use_corrected = False
    else:
        use_corrected = True

    args.output.parent.mkdir(exist_ok=True, parents=True)
    format_partition(args.input, args.output, args.rule_set, use_corrected,
                     args.procs, args.e2e_og)

if __name__ == '__main__':
    main()
