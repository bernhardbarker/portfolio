"""
https://leetcode.com/problems/combination-sum-ii

40. Combination Sum II (Medium)

Problem statement:

Given a collection of candidate numbers (candidates) and a target number (target), find all unique
combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """
    Generate all combinations that sum to some given target, by iteratively generating the
    combinations summing up to every value from 0 to target. Each number in `candidates` is only
    used once. Numbers that appear multiple times in `candidates` may appear up to the same number
    of times in a combination.
    """
    sum_to_combinations: list[list[list[int]]] = [[] for _ in range(target + 1)]

    sum_to_combinations[0] = [[]]
    # Sort candidates so duplicate candidates are adjacent
    candidates.sort()
    # How many times we've seen the same candidate
    duplicates = 0
    last = -1
    for candidate in candidates:
        if candidate == last:
            duplicates += 1
        else:
            duplicates = 0
        last = candidate

        # Iterate from back to front to avoid adding the same element multiple times
        for i in range(target - candidate, -1, -1):
            # Generate stc[5] = [[2, 3]] from stc[2] == [[2]] and candidate == 3
            # To avoid duplicates: if we've seen the same candidate already, we should only add this
            # one to combinations where the candidate already exists (in a quantity up to the number
            # of times we've seen it before)
            sum_to_combinations[i + candidate].extend([comb + [candidate]
                                                       for comb in sum_to_combinations[i]
                                                       if duplicates == sum(1 for c in comb
                                                                            if c == candidate)])

    return sum_to_combinations[target]

