"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
https://leetcode.com/problems/3sum/
"""

from typing import List


# expect O(n^2)
# python tada/tada_a_bigoh.py --directory ../speed-surprises/ --module speedsurprises.leetcode.three_sum --function two_pointers --types hypothesis --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json --startsize 50
# +----------------------------------------------------------------------------+
# |                        three_sum: O(n^2) quadratic                         |
# +------+------------------------+-----------------------+--------------------+
# | Size |          Mean          |         Median        |       Ratio        |
# +------+------------------------+-----------------------+--------------------+
# |  50  | 0.00034385338541666666 | 0.0003279850585937501 |         0          |
# | 100  | 0.0014534768880208333  | 0.0014072640624999992 | 4.227025091695906  |
# | 200  |  0.005029790104166667  |  0.004756653125000003 | 3.4605229334025522 |
# | 400  |  0.022569388958333332  |  0.021958287499999993 | 4.4871432984125725 |
# | 800  |  0.09099614083333332   |  0.08737992500000002  | 4.031838921351686  |
# +------+------------------------+-----------------------+--------------------+
def two_pointers(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            two_sum_two_pointers(nums, i, res)
    return res

def two_sum_two_pointers(nums: List[int], i: int, res: List[List[int]]):
    lo, hi = i + 1, len(nums) - 1
    while (lo < hi):
        sum = nums[i] + nums[lo] + nums[hi]
        if sum < 0:
            lo += 1
        elif sum > 0:
            hi -= 1
        else:
            res.append([nums[i], nums[lo], nums[hi]])
            lo += 1
            hi -= 1
            while lo < hi and nums[lo] == nums[lo - 1]:
                lo += 1


# expected O(n^2)
# python tada/tada_a_bigoh.py --directory ../speed-surprises/ --module speedsurprises.leetcode.three_sum --function hashset --types hypothesis --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json --startsize 50 --log
# +---------------------------------------------------------------------------+
# |                         hashset: O(n^2) quadratic                         |
# +------+-----------------------+-----------------------+--------------------+
# | Size |          Mean         |         Median        |       Ratio        |
# +------+-----------------------+-----------------------+--------------------+
# |  50  | 0.0005911650325520833 | 0.0005850060546875001 |         0          |
# | 100  | 0.0022075527604166665 | 0.0020985562499999996 | 3.7342410982709384 |
# | 200  |  0.008710804583333334 |  0.008251362499999998 | 3.945910031925672  |
# | 400  |  0.03780521666666667  |  0.03717572499999999  | 4.340037284156348  |
# | 800  |  0.15000015500000002  |  0.14246939999999997  | 3.9677104967436154 |
# +------+-----------------------+-----------------------+--------------------+
def hashset(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            two_sum_hashset(nums, i, res)
    return res


def two_sum_hashset(nums: List[int], i: int, res: List[List[int]]):
    seen = set()
    j = i + 1
    while j < len(nums):
        complement = -nums[i] - nums[j]
        if complement in seen:
            res.append([nums[i], nums[j], complement])
            while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                j += 1
        seen.add(nums[j])
        j += 1


# expected O(n^2)
# +----------------------------------------------------------------------------+
# |                         no_sort: O(n^2) quadratic                          |
# +------+------------------------+-----------------------+--------------------+
# | Size |          Mean          |         Median        |       Ratio        |
# +------+------------------------+-----------------------+--------------------+
# |  50  | 0.00039599344726562506 | 0.0003812200195312499 |         0          |
# | 100  | 0.0015199858333333333  | 0.0014877265625000014 | 3.838411579355643  |
# | 200  |  0.006000272760416667  |     0.00571868125     | 3.947584660876774  |
# | 400  |  0.023770679375000003  |  0.022637143750000005 | 3.9615998012312583 |
# +------+------------------------+-----------------------+--------------------+
def no_sort(nums: List[int]) -> List[List[int]]:
    res, dups = set(), set()
    seen = {}
    for i, val1 in enumerate(nums):
        if val1 not in dups:
            dups.add(val1)
            for j, val2 in enumerate(nums[i+1:]):
                complement = -val1 - val2
                if complement in seen and seen[complement] == i:
                    res.add(tuple(sorted((val1, val2, complement))))
                seen[val2] = i
    return res