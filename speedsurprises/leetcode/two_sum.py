"""
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.
https://leetcode.com/problems/two-sum/
"""

from typing import List


# Quit due to end of rounds:  6
# +------+------------------------+------------------------+---------------------+
# | Size |          Mean          |         Median         |        Ratio        |
# +------+------------------------+------------------------+---------------------+
# |  25  |  3.87159224802653e-06  | 3.845497406005861e-06  |          0          |
# |  50  | 5.014478346761068e-06  |  5.00479328918457e-06  |  1.2951979510024854 |
# | 100  | 1.475171777750651e-05  | 1.4665736877441402e-05 |  2.941825003000538  |
# | 200  | 5.2445819951375325e-06 |  5.15142855834961e-06  | 0.35552347694276637 |
# | 400  | 6.943884833170573e-05  | 6.770491088867188e-05  |  13.240111108203731 |
# | 800  | 1.3774474481201173e-05 | 1.3355961486816403e-05 | 0.19836841785453055 |
# +------+------------------------+------------------------+---------------------+
# O(1) constant or O(logn) logarithmic
def two_sum_linear(nums: List[int], target: int) -> List[int]:
    """O(n) solution"""
    seen = {}

    for index, num in enumerate(nums):
        other = target - num

        if other in seen:
            return [seen[other], index]

        seen[num] = index

    return []


# Quit due to indicator:  0.08552087409158471
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  25  | 3.0383726505533854e-05 | 3.0043125000000012e-05 |         0          |
# |  50  | 0.0001064639823404948  | 0.00010553764794921875 | 3.503980406126427  |
# | 100  | 0.00033685573551432295 | 0.00033546279492187504 | 3.1640347102270288 |
# | 200  | 0.00039986033808593754 |  0.00039556487890625   | 1.1870373454541807 |
# +------+------------------------+------------------------+--------------------+
# O(1) constant or O(logn) logarithmic
def two_sum_quadratic(nums: List[int], target: int) -> List[int]:
    """O(n^2) brute force"""
    for i, num in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - num:
                return [i, j]
    return []
