"""
Given a set of distinct integers, nums, return all possible subsets (the power
set). The solution set must not contain duplicate subsets.
https://leetcode.com/problems/subsets/
"""


# Expected O(N * 2^N)
# python tada/tada_a_bigoh.py --directory ../speed-surprises/ --module speedsurprises.leetcode.subsets --function subsets_backtrack --types hypothesis --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json --startsize 5  --log
# Quit due to exceeding the max time limit: 291.42858028411865
# +----------------------------------------------------------------------------+
# |                   subsets_backtrack: O(c^n) exponential                    |
# +------+-----------------------+------------------------+--------------------+
# | Size |          Mean         |         Median         |       Ratio        |
# +------+-----------------------+------------------------+--------------------+
# |  5   | 2.646700948079427e-05 | 2.4691595458984378e-05 |         0          |
# |  10  | 0.0010037408203125001 | 0.0009354132812499994  | 37.924224912560014 |
# |  20  |   1.6858900766666667  |   1.6647631500000002   |  1679.60696880076  |
# +------+-----------------------+------------------------+--------------------+
def subsets_backtrack(nums):
    """A backtracking approach to the subsets problem."""
    output = []

    def backtrack(so_far, rest):
        if not rest:
            output.append(so_far)
            return
        else:
            backtrack(so_far + [rest[0]], rest[1:])
            backtrack(so_far, rest[1:])

    backtrack([], nums)
    return output


# Expected O(N * 2^N)
# python tada/tada_a_bigoh.py --directory ../speed-surprises/ --module speedsurprises.leetcode.subsets --function subsets_iterative --types hypothesis --schema ../speed-surprises/speedsurprises/jsonschema/single_int_list.json --startsize 5  --log
# Quit due to exceeding the max time limit: 221.79610466957092
# +-----------------------------------------------------------------------------+
# |                    subsets_iterative: O(c^n) exponential                    |
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  5   | 6.921485544840495e-06  | 6.849217224121098e-06  |         0          |
# |  10  | 0.00027883302734374996 | 0.00026323359374999956 | 40.28514190159674  |
# |  20  |   0.7628617983333333   |       0.74831505       | 2735.9090334476937 |
# +------+------------------------+------------------------+--------------------+
def subsets_iterative(nums):
    """An iterative approach to the subsets problem."""
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]

    return output
