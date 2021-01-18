#!/usr/bin/env python

import argparse
import json
from pathlib import Path
from warnings import warn
import shutil
import tempfile
import random
from collections import defaultdict
import numpy as np
from itertools import permutations

import mrt.e2e.mr_utils
import mrt.viggo.mr_utils
from mrt.dialog_planner.bglm import beam_decode


def get_rule_set(rule_set):
    if rule_set == "E2E":
        mr_utils = mrt.e2e.mr_utils
    elif rule_set == 'Viggo':
        mr_utils = mrt.viggo.mr_utils
    else:
        raise Exception(f'Bad rule set: {rule_set}')
    return mr_utils
 
def bigram_iter(items):
    return zip(['@'] + list(items), list(items) + ['@'])

def lm_score(items, lm):
    return sum(lm[t1][t2] for t1, t2 in bigram_iter(items))
 
def get_canonical_orders(path, mr_utils, freq_info, slot_only=False):

    freq = defaultdict(lambda : defaultdict(int))
    for ex in example_iter(path):
        
        oracle_order = tuple(mr_utils.remove_header(
            ex['source']['sequence']['rule_delex']))
        canon_rep = tuple(sorted(oracle_order))

        if slot_only:
            oracle_order = tuple([x.split('=')[0] for x in oracle_order])
            canon_rep = tuple([x.split('=')[0] for x in canon_rep])

        freq[canon_rep][oracle_order] += 1

    lp_key = 'slot_transition_log_probs' if slot_only else \
        'slot_filler_transition_log_probs'
    co2sfo = {}
    for canon_order, freqs in freq.items():
        max_freq = max(freqs.values())
        
        max_items = [item for item in freqs.items() if item[1] == max_freq]
        if len(max_items) == 1:
            co2sfo[canon_order] = max_items[0][0]
        else:
            lm_scores = [lm_score(item[0], freq_info[lp_key]) 
                         for item in max_items]
            I = np.argsort(lm_scores)            
            co2sfo[canon_order] = max_items[I[-1]][0]
    return co2sfo

def find_best_constrained_perm(sf_items, s_order, lm):

    platforms = [x for x in sf_items if x.startswith('platforms')]
    genres = [x for x in sf_items if x.startswith('genres')]
    perspectives = [x for x in sf_items 
                    if x.startswith('player_perspective')]
    
    m = {sf.split("=")[0]: sf.split('=')[1] for sf in sf_items
         if sf.split('=')[0] not in ['platforms', 'genres', 'player_perspective']}

    best_score = float('-inf')
    best_perm = None
    for platforms_p in permutations(platforms):
        for genres_p in permutations(genres):
            for perspectives_p in permutations(perspectives):
                platforms_l = list(platforms_p)
                genres_l = list(genres_p)
                perspectives_l = list(perspectives_p)
                p = {
                    'platforms': list(platforms_p),
                    'genres': list(genres_p),
                    'player_perspective': list(perspectives_p),
                }
                sf_tmp = list(s_order)
                sf_order = [
                    (x+"=" + m[x] if x in m else p[x].pop(0))
                    for x in sf_tmp
                ]
                score = lm_score(sf_order, lm)
                if score > best_score:
                    best_score = score
                    best_perm = sf_order
    return best_perm

def generate_greedy_lm(sf_items, lm):
    inputs = list(sf_items)
    output = []
    t1 = '@'
    while inputs:
        scores = [lm[t1][t2] for t2 in inputs]
        idx = np.argmax(scores)
        t1 = inputs.pop(idx)
        output.append(t1)

    assert set(sf_items) == set(output)
    return output

#def add_orders(path, mr_utils, freq_info, slot_filler_canonical_order,
#               slot_canonical_order, use_orig_mr=False):
def add_orders(path, mr_utils, freq_info, lm, use_orig_mr=False):
    XXX = 0
    with tempfile.NamedTemporaryFile('w') as tmp_file:
        for example in example_iter(path):

            # Add corrected MR from rule based tagger.
            sf_seq = example['source']['sequence']['rule_lex']
            new_mr = mr_utils.linear_mr2mr(sf_seq)
            
            example['source']['mr'] = new_mr

            if use_orig_mr:
                MR = example['orig']['mr']
            else:    
                MR = example['source']['mr']

            # Add simple frequency based orderings.
            SEQS = example['source']['sequence'] 

            # Add random order.
            rs = random.getstate()
            linear_mr_lex_rnd = mr_utils.linearize_mr(
                MR, order='random')
            random.setstate(rs)
            linear_mr_delex_rnd = mr_utils.linearize_mr(
                MR, order='random', delex=True)
            SEQS['random_lex'] = linear_mr_lex_rnd
            SEQS['random_delex'] = linear_mr_delex_rnd
            
            # Add increasing frequency order.   
            linear_mr_lex_if = mr_utils.linearize_mr(
                MR, order='inc_freq', freq_info=freq_info)
            linear_mr_delex_if = mr_utils.linearize_mr(
                MR, order='inc_freq', freq_info=freq_info, delex=True)
            SEQS['inc_freq_lex'] = linear_mr_lex_if
            SEQS['inc_freq_delex'] = linear_mr_delex_if

            # Add decreasing frequency order.   
            linear_mr_lex_df = mr_utils.linearize_mr(
                MR, order='dec_freq', freq_info=freq_info)
            linear_mr_delex_df = mr_utils.linearize_mr(
                MR, order='dec_freq', freq_info=freq_info, delex=True)
            SEQS['dec_freq_lex'] = linear_mr_lex_df
            SEQS['dec_freq_delex'] = linear_mr_delex_df

            # Make increasing frequency fixed orders.
            linear_mr_lex_iff = mr_utils.linearize_mr(
                MR, order='inc_freq_fixed', freq_info=freq_info)
            linear_mr_delex_iff = mr_utils.linearize_mr(
                MR, order='inc_freq_fixed', freq_info=freq_info, delex=True)
            SEQS['inc_freq_fixed_lex'] = linear_mr_lex_iff
            SEQS['inc_freq_fixed_delex'] = linear_mr_delex_iff

            # Make decreasing frequency fixed orders.
            linear_mr_lex_dff = mr_utils.linearize_mr(
                MR, order='dec_freq_fixed', 
                freq_info=freq_info)
            linear_mr_delex_dff = mr_utils.linearize_mr(
                MR, order='dec_freq_fixed', 
                freq_info=freq_info, delex=True)
            SEQS['dec_freq_fixed_lex'] = linear_mr_lex_dff
            SEQS['dec_freq_fixed_delex'] = linear_mr_delex_dff

            freq_order_delex = beam_decode(
                lm, mr_utils.remove_header(SEQS['inc_freq_delex']), beam_size=32)

            freq_order_lex = []
            for sf in freq_order_delex:
                if sf.endswith("PLACEHOLDER") or sf.startswith('specifier'):
                    slot = sf.split('=')[0]
                    filler = MR['slots'][slot]
                    if "|" in filler:
                        filler = filler.split("|")[0]

                    freq_order_lex.append(f'{slot}={filler}')
                else:
                    freq_order_lex.append(sf)
            freq_order_delex = mr_utils.mr2header(MR) + list(freq_order_delex)
            freq_order_lex = mr_utils.mr2header(MR) + list(freq_order_lex)

            SEQS['bglm_lex'] = freq_order_lex
            SEQS['bglm_delex'] = freq_order_delex

#            if set(SEQS['freq_lex']) != set(SEQS['rule_lex']):
#                print(example['orig']['mr'])
#                print(example['target']['reference'])
#                print(SEQS['freq_lex'])
#                print(SEQS['rule_lex'])
#                input()

            print(json.dumps(example), file=tmp_file)
        tmp_file.flush()
        shutil.copy2(tmp_file.name, str(path)) 

def example_iter(path):
    with path.open("r") as fp:
        for line in fp:
            yield json.loads(line)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('rule_set', choices=['Viggo', 'E2E'])
    parser.add_argument("freqs", type=Path)
    parser.add_argument("inputs", type=Path)

    parser.add_argument('--test', action='store_true')
    #parser.add_argument("valid", type=Path)
    #parser.add_argument("test", type=Path)
    parser.add_argument("--seed", default=917601650175, type=int)

    args = parser.parse_args()

    random.seed(args.seed)

    # Load counts info and mr utils 
    freq_info = json.loads(args.freqs.read_text())
    mr_utils = get_rule_set(args.rule_set)
    lm = freq_info['slot_filler_transition_log_probs']

#    # Get canonical order mappings for slot filler seqs and slot seqs.
#    slot_filler_canonical_order = get_canonical_orders(
#        args.train, mr_utils, freq_info)
#
#    slot_canonical_order = get_canonical_orders(
#        args.train, mr_utils, freq_info, slot_only=True)


    # Add orders to datasets.
    add_orders(args.inputs, mr_utils, freq_info, lm, use_orig_mr=args.test)
           #    slot_filler_canonical_order, slot_canonical_order)
#    add_orders(args.valid, mr_utils, freq_info, lm)
#           #    slot_filler_canonical_order, slot_canonical_order)
#    add_orders(args.test, mr_utils, freq_info, lm, use_orig_mr=True)
             #  slot_filler_canonical_order, slot_canonical_order,
             #  use_orig_mr=True)

if __name__ == "__main__":
    main()
