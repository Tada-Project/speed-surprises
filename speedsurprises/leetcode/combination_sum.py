"""Given an array of distinct integers candidates and a target integer
target, return a list of all unique combinations of candidates where the
chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen
numbers is different.

It is guaranteed that the number of unique combinations that sum up to
target is less than 150 combinations for the given input.
https://leetcode.com/problems/combination-sum/
"""

from typing import List


# python tada/tada_a_bigoh.py --directory ../speed-surprises/ --module speedsurprises.leetcode.combination_sum --function combination_sum --types hypothesis --schema ../speed-surprises/speedsurprises/jsonschema/list_and_int0.json --startsize 50  --log
def combination_sum(candidates: List[int], target: int) -> List[List[int]]:

    results = []

    def backtrack(remain, comb, start):
        if remain == 0:
            # make a deep copy of the current combination
            results.append(list(comb))
            return
        elif remain < 0:
            # exceed the scope, stop exploration.
            return

        for i in range(start, len(candidates)):
            # add the number into the combination
            comb.append(candidates[i])
            # give the current number another chance, rather than moving on
            backtrack(remain - candidates[i], comb, i)
            # backtrack, remove the number from the combination
            comb.pop()

    backtrack(target, [], 0)

    return results