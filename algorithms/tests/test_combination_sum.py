""" Test module for Combination Sum """

from parameterized import parameterized

from algorithms.combination_sum import combination_sum

@parameterized.expand([
    ([2,3,6,7], 7, [[2,2,3], [7]]),
    ([2,3,5], 8, [[2,2,2,2], [2,3,3], [3,5]]),
    ([2], 1, []),
])
def test_combination_sum(candidates: list[int], target: int, expected: list[list[int]]) -> None:
    """ Test function """
    solution = combination_sum(candidates, target)
    assert sorted([sorted(x) for x in solution]) == expected
    print(f"candidates = {str(candidates):12s}, target = {target}"
          " returned correct result of {expected}")
