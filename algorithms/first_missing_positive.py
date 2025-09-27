"""
https://leetcode.com/problems/first-missing-positive

41. First Missing Positive (Hard)

Problem statement:

Given an unsorted integer array nums. Return the smallest positive integer that is not present in
nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
"""

def first_missing_positive(nums: list[int]) -> int:
    """ Find the first missing positive integer """
    # Define an element's "correct" position to be such that nums[i-1] = i
    # For each index in the list:
    # - Repeatedly swap that index's element with the element at its correct position
    # - Stop when the given element is already in its correct position, when the target position is
    #   outside the list or when the target position's element equals to the current element
    for i, val in enumerate(nums):
        while val-1 != i and 0 < val <= len(nums) and nums[val-1] != nums[i]:
            nums[val-1], nums[i] = nums[i], nums[val-1]
            val = nums[i]

    # Return the index of the first element not in its correct position
    for i, val in enumerate(nums):
        if val-1 != i:
            return i + 1

    # If no incorrect position was found, the list contains elements 1 to `len(nums)`, so the first
    # missing positive integer is `len(nums) + 1`
    return len(nums) + 1
