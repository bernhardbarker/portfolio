"""
https://leetcode.com/problems/combination-sum

39. Combination Sum (Medium)

Problem statement:

Given an array of distinct integers candidates and a target integer target, return a list of all
unique combinations of candidates where the chosen numbers sum to target. You may return the
combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are
unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is
less than 150 combinations for the given input.
"""

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    """
    Generate all combinations that sum to some given target, by iteratively generating the
    combinations summing up to every value from 0 to target.
    """
    # A list of combinations such that `stc[5] = [[2, 3], [1, 4]]` means 2+3 and 1+4 both give 5
    sum_to_combinations: list[list[list[int]]] = [[] for _ in range(target + 1)]

    sum_to_combinations[0] = [[]]
    for candidate in candidates:
        for i in range(target - candidate + 1):
            # Generate stc[5] = [[2, 3]] from stc[2] == [[2]] and candidate == 3
            # Since we run through each candidates across the entire list before moving on to the
            # next candidate, we avoid the duplication of generating stc[5] = [[3, 2]] from
            # stc[3] == [[3]] and candidate == 2
            sum_to_combinations[i + candidate].extend([comb + [candidate]
                                                       for comb in sum_to_combinations[i]])

    return sum_to_combinations[target]
