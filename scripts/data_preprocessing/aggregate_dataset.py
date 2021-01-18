#!/usr/bin/env python

import argparse
from pathlib import Path
import json
from collections import defaultdict
import numpy as np
from copy import deepcopy

import mrt.viggo.mr_utils
import mrt.e2e.mr_utils


def get_rule_set(rule_set):
    if rule_set == "E2E":
        mr_utils = mrt.e2e.mr_utils
    elif rule_set == 'Viggo':
        mr_utils = mrt.viggo.mr_utils
    else:
        raise Exception(f'Bad rule set: {rule_set}')
    return mr_utils
 
def example_iter(path):
    with path.open("r") as fp:
        for line in fp:
            yield json.loads(line)

def to_bigrams(seq):
    bigrams = set()
    for t1, t2 in zip(['@'] + seq, seq + ['@']):
        bigrams.add((t1, t2))
    return bigrams

def seq_sim(s1, s2):
    return len(s1.intersection(s2)) / len(s1)

def get_best_rule_seq(seqs):

    if len(seqs) == 1:
        return seqs[0]

    seq_bigrams = [to_bigrams(s) for s in seqs]

    sims = []
    for i, seq_i in enumerate(seq_bigrams):
        sims.append(
            [
                seq_sim(seq_i, seq_j) for j, seq_j in enumerate(seq_bigrams)
                if i != j
            ]
        )
    sims = np.array(sims).mean(axis=1)
    return seqs[np.argmax(sims)]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('rule_set', choices=['Viggo', 'E2E'])
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()
    print(f"is-test: {args.test}")

    mr_utils = get_rule_set(args.rule_set)


    mr2examples = defaultdict(list)
    for example in example_iter(args.input):
        if args.test:
            mr = example['orig']['mr']
        else:
            mr = example['source']['mr']
        lmr = mr_utils.linearize_mr(mr)
        canonical_lmr = tuple(sorted(set(lmr)))
        mr2examples[canonical_lmr].append(example)

    args.output.parent.mkdir(exist_ok=True, parents=True)
    with args.output.open('w') as fp:
        for clmr, examples in mr2examples.items():
            orig = examples[0]['orig']
            source = deepcopy(examples[0]['source'])
            targets = {
                'targets': [ex['target'] for ex in examples],
                'reference_strings': '\n'.join(
                    [ex['target']['reference'] for ex in examples])
            }
            
            max_rule_delex_lens = max([len(x['source']['sequence']['rule_delex'])
                                       for x in examples])
            rule_delex_seqs = [] 
            for ex in examples:
                if len(ex['source']['sequence']['rule_delex'])  == max_rule_delex_lens:
                    rule_delex_seqs.append(ex['source']['sequence']['rule_delex'])
            best_rule_delex_seq = get_best_rule_seq(rule_delex_seqs)
            source['sequence']['rule_delex'] = best_rule_delex_seq

            max_rule_lex_lens = max([len(x['source']['sequence']['rule_lex'])
                                     for x in examples])
            rule_lex_seqs = [] 
            for ex in examples:
                if len(ex['source']['sequence']['rule_lex']) == max_rule_lex_lens:
                    rule_lex_seqs.append(ex['source']['sequence']['rule_lex'])
            best_rule_lex_seq = get_best_rule_seq(rule_lex_seqs)
            source['sequence']['rule_lex'] = best_rule_lex_seq

            for ex in examples:
                if ex['source']['sequence']['rule_lex'] == best_rule_lex_seq:
                    source['sequence']['bglm_lex'] = \
                        ex['source']['sequence']['bglm_lex']
                    break

            for ex in examples:
                if ex['source']['sequence']['rule_delex'] == best_rule_delex_seq:
                    source['sequence']['bglm_delex'] = \
                        ex['source']['sequence']['bglm_delex']
                    break

            agg_example = {
                'orig': orig,
                'source': source, 
                'target': targets,
            }
            print(json.dumps(agg_example), file=fp)

if __name__ == '__main__':
    main()
