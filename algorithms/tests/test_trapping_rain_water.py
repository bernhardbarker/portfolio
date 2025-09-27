""" Test module for Trapping Rain Water """

from parameterized import parameterized

from algorithms.trapping_rain_water import calculate_trapped_rain_water

@parameterized.expand([
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5], 9),
    ([0], 0),
    ([10], 0),
    ([10,10], 0),
])
def test_calculate_trapped_rain_water(heights: list[int], expected: int) -> None:
    """ Test function """
    result = calculate_trapped_rain_water(heights)
    assert result == expected
    print(f"heights = {str(heights):36s} returned correct result of {expected}")
