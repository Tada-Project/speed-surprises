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

# Expected O(n) --> target number 0, minimum value 1, the max depth of the tree is 0/1 = 0, size n, O(n^(0/1 + 1)) == O(n)
# Quit due to indicator: 0.05422886313000301
# +-----------------------------------------------------------------------------+
# |            combination_sum: O(1) constant or O(logn) logarithmic            |
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 1.0193872210184734e-06 | 1.0079918403625495e-06 |         0          |
# | 100  | 1.136286982345581e-06  | 1.1032247886657717e-06 | 1.1146765026250893 |
# +------+------------------------+------------------------+--------------------+
# python tada/tada_a_bigoh.py --directory ../speed-surprises/ --module speedsurprises.leetcode.combination_sum --function combination_sum --types hypothesis --schema ../speed-surprises/speedsurprises/jsonschema/list_and_int0.json --startsize 50  --log
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


# iterative approach by TheOliveKing ()
# Quit due to exceeding the max time limit: 241.933278799057
# +-----------------------------------------------------------------------------+
# |           combination_sum_2: O(n) linear or O(nlogn) linearithmic           |
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 2.403005523681641e-06  | 2.3799171447753903e-06 |         0          |
# | 100  | 3.5623719278971344e-06 | 3.3786392211914007e-06 | 1.4824651432507863 |
# | 200  |  5.34920639038086e-06  |  5.1771224975586e-06   | 1.5015856004509032 |
# | 400  | 9.215837097167971e-06  | 8.906381225585929e-06  | 1.722841936654422  |
# +------+------------------------+------------------------+--------------------+
def combination_sum_2(nums, target):
    res = []
    nums.sort()
    def dfs(left, path, idx):
        if not left: res.append(path[:])
        else:
            for i, val in enumerate(nums[idx:]):
                if val > left: break
                dfs(left - val, path + [val], idx + i)
    dfs(target, [], 0)
    return res


# Expect O(target^n), when target = 0, expect O(0) -> O(1)
# Quit due to indicator: 0.08334973111885821
# +-----------------------------------------------------------------------------+
# |           combination_sum_3: O(1) constant or O(logn) logarithmic           |
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 1.0524142328898111e-06 | 1.0113208770751972e-06 |         0          |
# | 100  | 8.904749425252276e-07  | 8.188911437988271e-07  | 0.8461259024216002 |
# +------+------------------------+------------------------+--------------------+
# Expect O(target^n), when target = 2, expect O(2^n)
# Quit due to exceeding the max time limit: 218.99578046798706
# +-----------------------------------------------------------------------------+
# |           combination_sum_3: O(n) linear or O(nlogn) linearithmic           |
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 2.165257954915364e-05  | 2.2129180908203122e-05 |         0          |
# | 100  | 4.0806046956380206e-05 | 3.9891479492187507e-05 | 1.8845813203801502 |
# | 200  | 8.048438639322919e-05  | 7.975593261718751e-05  | 1.9723642057086126 |
# | 400  | 0.00015408850260416665 |  0.000146213232421875  | 1.914514224551875  |
# +------+------------------------+------------------------+--------------------+
# Expect O(target^n), when target = 10, expect O(10^n)
# Quit due to reaching max size: 800
# +-----------------------------------------------------------------------------+
# |           combination_sum_3: O(n) linear or O(nlogn) linearithmic           |
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 0.00010718274739583332 |  0.00010633818359375   |         0          |
# | 100  | 0.00023987938476562499 | 0.00023283164062499985 | 2.238041014938102  |
# | 200  | 0.00045949762369791667 | 0.00044007441406249907 | 1.9155361105618578 |
# | 400  | 0.0009439356640625003  |  0.000940825000000001  | 2.0542775748565423 |
# | 800  | 0.0017669477083333339  | 0.0017491812500000023  | 1.8718942144094473 |
# +------+------------------------+------------------------+--------------------+
# Not use hypothesis
# Quit due to reaching max size: 5000
# +-----------------------------------------------------------------------------+
# |           combination_sum_3: O(n) linear or O(nlogn) linearithmic           |
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 0.00015862659016927078 | 0.00015460317382812476 |         0          |
# | 100  |  0.000350165341796875  |    0.00033685390625    | 2.207481995441072  |
# | 200  |   0.0006715715234375   | 0.0006516623046874991  | 1.9178697697245757 |
# | 400  | 0.0013392686328125001  | 0.0013288937500000007  | 1.9942308243764293 |
# | 800  | 0.0026380645052083334  | 0.0025602249999999993  | 1.9697799534573786 |
# | 1600 |  0.005494970572916666  |     0.00536869375      | 2.082955349297919  |
# | 3200 |  0.01089633666666667   |  0.010650296875000007  | 1.9829654266707057 |
# +------+------------------------+------------------------+--------------------+

def combination_sum_3(candidates: List[int], target: int) -> List[List[int]]:
    if len(candidates) == 0:
        return []
    dp = {}
    dp[0] = [[]]
    
    for i in range(1,target+1):
        output = []
        for j in range(len(candidates)):
            if (i - candidates[j]) >= 0 and (i - candidates[j]) in dp:
                prev_path = dp.get(i-candidates[j])
        
                for each in prev_path:
                    temp = sorted(each+[candidates[j]])
                    if temp not in output:
                        output.append(temp)
        if output:
            dp[i] = output
            
    if target not in dp:
        return []
    return dp[target]