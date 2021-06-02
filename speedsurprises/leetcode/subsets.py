"""
Given a set of distinct integers, nums, return all possible subsets (the power
set). The solution set must not contain duplicate subsets.
https://leetcode.com/problems/subsets/
"""


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


def subsets_iterative(nums):
    """An iterative approach to the subsets problem."""
    output = [[]]

    for num in nums:
        output += [curr + [num] for curr in output]

    return output
