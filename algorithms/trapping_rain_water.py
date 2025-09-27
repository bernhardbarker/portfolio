"""
https://leetcode.com/problems/trapping-rain-water

42. Trapping Rain Water (Hard)

Problem statement:

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""

def calculate_trapped_rain_water(heights: list[int]) -> int:
    """
    Find the amount of trapped water by finding the tallest height to the left and right and taking
    the minimum of that for each element
    """
    tallest_left = [0] * len(heights)
    tallest_left[0] = heights[0]
    for i, height in enumerate(heights):
        tallest_left[i] = max(tallest_left[i-1], height)
    tallest_right = heights[-1]
    total_water = 0
    # Loop over elements, excluding first and last element
    for i in range(len(heights)-2, 0, -1):
        tallest_right = max(tallest_right, heights[i])
        total_water += min(tallest_left[i], tallest_right) - heights[i]
    return total_water
