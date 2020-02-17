"""
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.
https://leetcode.com/problems/two-sum/
"""

from typing import List


def two_sum_linear(nums: List[int], target: int) -> List[int]:
    """O(n) solution"""
    seen = {}

    for index, num in enumerate(nums):
        other = target - num

        if other in seen:
            return [seen[other], index]

        seen[num] = index

    return []


def two_sum_quadratic(nums: List[int], target: int) -> List[int]:
    """O(n^2) brute force"""
    for i, num in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - num:
                return [i, j]
    return []
