#!/usr/bin/env python

import argparse
from pathlib import Path
import json

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

def load_test_mrs(path, mr_utils):
    mrs = set()
    for example in example_iter(path):
        mr = example['orig']['mr']
        lmr = mr_utils.linearize_mr(mr)
        canonical_lmr = tuple(sorted(set(lmr)))
        mrs.add(canonical_lmr)
    return mrs

def filter_test_mrs(in_path, out_path, test_mrs, mr_utils):

    total = 0
    filtered = 0
    out_path.parent.mkdir(exist_ok=True, parents=True)
    with out_path.open('w') as fp:
        for example in example_iter(in_path):
            total += 1
            mr = example['source']['mr']
            lmr = mr_utils.linearize_mr(mr)
            canonical_lmr = tuple(sorted(set(lmr)))

            if canonical_lmr not in test_mrs:
                print(json.dumps(example), file=fp)
            else:
                filtered += 1
    rem = total - filtered
    rem_pct = rem / total * 100

    print(
        f"Orig: {total}  Filtered: {filtered}  Final: {rem} ({rem_pct:5.2f}%)")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('rule_set', choices=['Viggo', 'E2E'])
    parser.add_argument("data_in", type=Path)
    parser.add_argument("data_out", type=Path)
    parser.add_argument("test", type=Path)
    args = parser.parse_args()

    mr_utils = get_rule_set(args.rule_set)
    test_mrs = load_test_mrs(args.test, mr_utils)

    filter_test_mrs(args.data_in, args.data_out, test_mrs, mr_utils)

if __name__ == '__main__':
    main()
