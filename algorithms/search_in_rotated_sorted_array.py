"""
https://leetcode.com/problems/search-in-rotated-sorted-array

33. Search in Rotated Sorted Array (Medium)

Problem statement:

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k 
(1 <= k < nums.length) such that the resulting array is:
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target
if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

def search(nums: list[int], target: int) -> int:
    """ Find index of target in rotated sorted array """
    left, right = 0, len(nums) - 1
    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    # Binary search to find the beginning of the sorted array before rotation
    while left < right:
        mid = (left + right + 1) // 2
        if nums[mid] < nums[left]:
            right = mid - 1
        else:
            left = mid

    # Check if the target value is on the left or right by comparing it to the first value
    if target < nums[0]:
        right = len(nums) - 1
    else:
        left, right = 0, left

    # Binary search to find the target value
    while left < right:
        mid = (left + right + 1) // 2
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid

    if target == nums[left]:
        return left

    return -1
