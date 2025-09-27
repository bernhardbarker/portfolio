""" Test module for Search in Rotated Sorted Array """

from parameterized import parameterized

from algorithms.search_in_rotated_sorted_array import search

@parameterized.expand([
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ([1], 0, -1),
    ([1, 3], 0, -1),
    ([1, 3], 1, 0),
    ([1, 3], 3, 1),
    ([3, 1], 3, 0),
])
def test_search(nums: list[int], target: int, expected: int) -> None:
    """ Test function """
    solution = search(nums, target)
    assert solution == expected
    print(f"nums = [{', '.join(map(str, nums)):19s}], target = {target}")
    print(f"\treturned correct result of {solution}")
