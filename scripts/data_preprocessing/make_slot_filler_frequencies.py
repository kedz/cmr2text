#!/usr/bin/env python

import argparse
from pathlib import Path
import json
from collections import defaultdict
import math

import mrt.e2e.mr_utils
import mrt.viggo.mr_utils


def bigram_iter(items):
    return zip(['@'] + list(items), list(items) + ['@'])

def get_rule_set(rule_set):
    if rule_set == "E2E":
        mr_utils = mrt.e2e.mr_utils
    elif rule_set == 'Viggo':
        mr_utils = mrt.viggo.mr_utils
    else:
        raise Exception(f'Bad rule set: {rule_set}')
    return mr_utils
 
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('rule_set', choices=['Viggo', 'E2E'])
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    
    mr_utils = get_rule_set(args.rule_set)

    slot_filler_counts = {}
    slot_counts = {}
    max_slot_lens = {}
    transition_counts = defaultdict(lambda: defaultdict(int))
    s_transition_counts = defaultdict(lambda: defaultdict(int))

    with args.input.open('r') as fp:
        for line in fp:
            ex = json.loads(line)
            sf_seq = mr_utils.remove_header(
                ex['source']['sequence']['rule_delex'])
            local_slot_counts = {}
            for sf in set(sf_seq):
                slot_filler_counts[sf] = slot_filler_counts.get(sf, 0) + 1
                slot, filler = sf.split('=')
                slot_counts[slot] = slot_counts.get(slot, 0) + 1
                local_slot_counts[slot] = local_slot_counts.get(slot, 0) + 1
            for slot, count in local_slot_counts.items():
                max_slot_lens[slot] = max(count, max_slot_lens.get(slot, 0))

            
            for t1, t2 in bigram_iter(sf_seq):
                transition_counts[t1][t2] += 1

            s_seq = [x.split("=")[0] for x in sf_seq]
            for t1, t2 in bigram_iter(s_seq):
                s_transition_counts[t1][t2] += 1

    # Explicitly put 0 transition pairs in.
    sf_vocab = ['@'] + list(slot_filler_counts.keys())

    eps = 1e-6
    transition_log_probs = defaultdict(lambda: defaultdict(float))
    for t1 in sf_vocab:
        # Make normalizer with Lidstone smoothing.
        norm = sum(transition_counts[t1].values()) + eps * len(sf_vocab)
        log_norm = math.log(norm)

        for t2 in sf_vocab:
            transition_log_probs[t1][t2] = (
                math.log(transition_counts[t1][t2] + eps) - log_norm
            )

    # Explicitly put 0 transition pairs in.
    s_vocab = ['@'] + list(slot_counts.keys())

    eps = 1e-6
    s_transition_log_probs = defaultdict(lambda: defaultdict(float))
    for t1 in s_vocab:
        # Make normalizer with Lidstone smoothing.
        norm = sum(s_transition_counts[t1].values()) + eps * len(s_vocab)
        log_norm = math.log(norm)

        for t2 in s_vocab:
            s_transition_log_probs[t1][t2] = (
                math.log(s_transition_counts[t1][t2] + eps) - log_norm
            )


    data = {
        'slot_counts': slot_counts,
        'list_slot_max_lengths': max_slot_lens,
        'delex_slot_filler_counts': slot_filler_counts,
        'slot_filler_transition_counts': transition_counts,
        'slot_filler_transition_log_probs': transition_log_probs,
        'slot_transition_counts': s_transition_counts,
        'slot_transition_log_probs': s_transition_log_probs,
    }
    data_json = json.dumps(data, indent='    ', sort_keys=True)
    
    if not args.output.exists() or (args.output.read_text() != data_json):
        args.output.parent.mkdir(exist_ok=True, parents=True)
        args.output.write_text(data_json)

if __name__ == '__main__':
    main()
