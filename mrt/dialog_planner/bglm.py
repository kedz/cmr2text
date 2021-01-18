import argparse
import json
from pathlib import Path

import numpy as np
from scipy import stats

import mrt.e2e.mr_utils
import mrt.viggo.mr_utils


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

def greedy_decode(lm, lmr, return_score=False):
    remaining = list(lmr)
    curr = "@"

    score = 0
    output = []
    while remaining:
        scores = [lm[curr][token] for token in remaining]
        next_score = max(scores)
        idx = scores.index(next_score)
        next_token = remaining.pop(idx)
        score += next_score
        output.append(next_token)
        curr = next_token
    score += lm[curr]["@"]
    if return_score:
        return output, score
    return output

def beam_decode(lm, lmr, beam_size=8, return_score=False):

    remaining = [list(lmr)]
    beam_scores = [0.]
    beam = [["@"]]

    T = 1
    while remaining[0]:
        candidates = []
        for b, item in enumerate(beam):
            cur_tkn = beam[b][-1]
            def st(x):
                return lm[cur_tkn][x]
            next_scores_tkn = [st(tkn) for tkn in remaining[b]]
            next_scores_seq = [beam_scores[b] + s for s in next_scores_tkn]
#            print(f"T={T}  Beam {b}")
#            print("next score (token)")
#            print(next_scores_tkn)
#            print("next_score (seq)")
#            print(next_scores_seq)

            next_idxs = np.argsort(next_scores_seq)[-beam_size:]
            
#            print(next_idxs)
            for idx in next_idxs:
                candidates.append((b, idx, next_scores_seq[idx]))
        
#        for c in candidates:
#            print(c)
        
        I = np.argsort([x[2] for x in candidates])
#        print(I)

        next_beam = []
        next_beam_scores = []
        next_beam_remaining = []
        for idx in I[-beam_size:]:
            next_beam_idx, next_choice, next_score = candidates[idx]
            
            next_rem = list(remaining[next_beam_idx])
            next_tkn = next_rem.pop(next_choice)
            next_beam_remaining = [next_rem] + next_beam_remaining

            next_beam = [beam[next_beam_idx] + [next_tkn]] + next_beam
            next_beam_scores = [next_score] + next_beam_scores

        beam = next_beam
        beam_scores = next_beam_scores
        remaining = next_beam_remaining

#        print()
#        for i in range(len(beam)):
#            print(i)
#            print(beam[i])
#            print(beam_scores[i])
#            print(remaining[i])
#            print()
#            
#
#        input()
            
        T += 1
    beam_scores = [s + lm[beam[b][-1]]["@"] 
                   for b, s in enumerate(beam_scores)]

    I = np.argsort(beam_scores)[::-1]
    beam = [beam[i] for i in I]
    beam_scores = [beam_scores[i] for i in I]
    remaining = [remaining[i] for i in I]

#    print()
#    for i in range(len(beam)):
#        print(f'{beam_scores[i]:8.4f}', list(beam[i][1:]))

    assert all([len(r) == 0 for r in remaining])

    if return_score:
        return list(beam[0][1:]), beam_scores[0]
    return list(beam[0][1:])    

    
def brute_force(lm, lmr):

    from itertools import permutations
    outputs = []
    for perm in permutations(lmr):
        score = 0
        for t1, t2 in zip(("@",) + perm, perm + ("@",)):
            score += lm[t1][t2]
        outputs.append((score, perm))
    outputs.sort(key=lambda x: x[0], reverse=True)
    for score, output in outputs[:5]:
        print(f'{score:8.4f}', list(output))

def eval_kt(true_y, pred_y):
    rank_map = {yi: i for i, yi in enumerate(pred_y)}
    true_ranks = [rank_map[yi] for yi in true_y]
    pred_ranks = [rank_map[yi] for yi in pred_y]
    kt, _ = stats.kendalltau(true_ranks, pred_ranks)
    return kt

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('rule_set', choices=['Viggo', 'E2E'])
    parser.add_argument("freqs", type=Path)
    parser.add_argument('ds', type=Path)


    args = parser.parse_args()

    mr_utils = get_rule_set(args.rule_set)
    freq_info = json.loads(args.freqs.read_text())

    use_fillers = True
 

    if use_fillers:
        lm = freq_info["slot_filler_transition_log_probs"]
    else:
        lm = freq_info['slot_transition_log_probs']

    greedy_kt = []
    beam_kt = []
    old_kt = []
    
    for ex in example_iter(args.ds):
        lmr = mr_utils.remove_header(ex['source']['sequence'][f'rule_delex'])
#        old_lmr = mr_utils.remove_header(ex['source']['sequence']['freq_delex'])
        if not use_fillers:
            lmr = [x.split('=')[0] for x in lmr]
#            old_lmr = [x.split('=')[0] for x in old_lmr]
        if len(set(lmr)) < 2:
            continue
        #print("GT")
        #print(lmr)
        #print()
        greedy = greedy_decode(lm, lmr)
        #print(greedy)
        greedy_kt.append(eval_kt(lmr, greedy))
        if greedy_kt[-1] != greedy_kt[-1]:
            print(ex['orig']['mr'])
            print(ex['source']['mr'])
            print(ex['target']['reference_strings'])
            input()

        #print(old_lmr)
        #print(lmr)
#        if len(lmr) == len(old_lmr) and all([x in old_lmr for x in lmr]):
#            old_kt.append(eval_kt([x for x in lmr if x in old_lmr], old_lmr))
#        print()
#        brute_force(lm, lmr)
        #print()
        beam = beam_decode(lm, lmr, beam_size=32)
        #print(beam)
        beam_kt.append(eval_kt(lmr, beam))
        #input()
   
    print(f"greedy kt: {np.mean(greedy_kt):0.3f}")
    print(f"  beam kt: {np.mean(beam_kt):0.3f}")
#    print(f"   old kt: {np.mean(old_kt):0.3f}")
#    print(len(old_kt))

if __name__ == "__main__":
    main()
