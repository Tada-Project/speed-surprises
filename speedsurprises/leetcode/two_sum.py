"""
Compute the solution to the two-sum problem.

Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.
"""

# Reference:
# https://leetcode.com/problems/two-sum/

from typing import List


# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.leetcode.two_sum --function=two_sum_linear --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_and_intdiff_twosum.json --startsize=25 --max=1000

# Quit due to indicator:  0.016086062325729705
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  25  |  4.18525400797526e-06  | 4.1738525390625016e-06 |         0          |
# |  50  | 7.214981791178385e-06  | 7.566503906250001e-06  | 1.7239053537562574 |
# | 100  | 1.158954854329427e-05  | 1.404320068359375e-05  | 1.606317088348661  |
# | 200  | 1.1222591044108072e-05 | 8.983409881591797e-06  | 0.9683372050416476 |
# +------+------------------------+------------------------+--------------------+
# O(1) constant or O(logn) logarithmic


def two_sum_linear(nums: List[int], target: int) -> List[int]:
    """Compute the O(n) solution."""
    seen = {}
    for index, num in enumerate(nums):
        other = target - num
        if other in seen:
            return [seen[other], index]
        seen[num] = index
    return []


# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.leetcode.two_sum --function=two_sum_quadratic --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_and_intdiff_twosum.json --startsize=25 --max=1000

# Quit due to researched max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  25  | 3.0287581380208332e-05 | 3.0213098144531256e-05 |         0          |
# |  50  | 6.183509114583333e-05  | 3.380620117187497e-05  | 2.041598844410864  |
# | 100  | 0.00021712490559895833 | 0.00022461484374999998 | 3.5113541773050168 |
# | 200  | 0.0002923348177083334  | 0.00022819335937499983 | 1.346390073961814  |
# | 400  | 0.00018583254557291668 | 0.00010028300781250016 | 0.6356839292346096 |
# | 800  | 0.00013153273803710936 | 9.277166748046875e-05  | 0.7078024876191493 |
# +------+------------------------+------------------------+--------------------+
# O(1) constant or O(logn) logarithmic

def two_sum_quadratic(nums: List[int], target: int) -> List[int]:
    """Compute the O(n^2) brute force solution."""
    for i, num in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - num:
                return [i, j]
    return []
