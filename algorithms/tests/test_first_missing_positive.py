""" Test module for First Missing Positive """

from parameterized import parameterized

from algorithms.first_missing_positive import first_missing_positive

@parameterized.expand([
    ([1,2,0], 3),
    ([3,4,-1,1], 2),
    ([7,8,9,11,12], 1),
    ([1], 2),
    ([1,2], 3),
    ([2,1], 3),
    ([1,1], 2),
])
def test_first_missing_positive(nums: list[int], expected: int) -> None:
    """ Test function """
    result = first_missing_positive(nums)
    assert result == expected
    print(f"nums = {str(nums):17s} returned correct result of {expected}")
