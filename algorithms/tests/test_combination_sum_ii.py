""" Test module for Combination Sum II """

from parameterized import parameterized

from algorithms.combination_sum_ii import combination_sum

@parameterized.expand([
    ([10,1,2,7,6,1,5], 8, [[1,1,6], [1,2,5], [1,7], [2,6]]),
    ([2,5,2,1,2], 5, [[1,2,2], [5]]),
    ([2], 1, []),
])
def test_combination_sum(candidates: list[int], target: int, expected: list[list[int]]) -> None:
    """ Test function """
    solution = combination_sum(candidates, target)
    assert sorted([sorted(x) for x in solution]) == expected
    print(f"candidates = {str(candidates):12s}, target = {target}"
          " returned correct result of {expected}")
