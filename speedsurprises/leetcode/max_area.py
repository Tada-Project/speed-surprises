"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms
a container, such that the container contains the most water.
https://leetcode.com/problems/container-with-most-water/
"""

from typing import List


# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.leetcode.max_area --function=max_area_linear --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=50 --max=1000
# Quit due to end of rounds:  5
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 3.3008806831868494e-05 | 3.1646433227539056e-05 |         0          |
# | 100  | 6.358826088053385e-05  | 6.273050073242188e-05  | 1.9264028901263492 |
# | 200  | 0.00012151662773437501 | 0.00012129220947265627 | 1.9109915266069912 |
# | 400  | 0.0002542096930338542  | 0.00024810891992187503 | 2.0919745533881575 |
# | 800  | 0.0005395804107421874  | 0.0005376722871093752  | 2.122580001976279  |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic
def max_area_linear(height: List[int]) -> int:
    """O(n) solution"""
    right = 0
    left = len(height) - 1
    max_container = 0
    while right < left:
        max_container = max(
            [max_container, min(height[right], height[left]) * abs(right - left)]
        )
        if height[right] > height[left]:
            left -= 1
        else:
            right += 1

    return max_container


# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.leetcode.max_area --function=max_area_log --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=50 --max=1000
# Quit due to end of rounds:  5
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 4.0933711356608075e-05 | 4.067579528808593e-05  |         0          |
# | 100  |  8.87667048421224e-05  | 8.656514965820313e-05  | 2.1685476811227984 |
# | 200  | 0.00018507136878255208 | 0.00018368952587890627 | 2.0849187666897633 |
# | 400  | 0.0004335159373046875  | 0.0004283158730468752  | 2.342425736387367  |
# | 800  | 0.0009118717535156251  |  0.00088876512890625   | 2.103433057582691  |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic
def max_area_log(height: List[int]) -> int:
    """O(nlogn) solution"""
    # pylint: disable=W1637, W1638
    X = zip(height, range(len(height)))
    X = list(sorted(X, reverse=True))
    L = X[0][1]
    R = L
    OPT = 0
    for H, P in X[1:]:
        L = min(L, P)
        R = max(R, P)
        OPT = max(OPT, H * (R - P), H * (P - L))
    return OPT


# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.leetcode.max_area --function=max_area_quadratic --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=50 --max=1000
# Quit due to end of rounds:  5
# +------+-----------------------+-----------------------+--------------------+
# | Size |          Mean         |         Median        |       Ratio        |
# +------+-----------------------+-----------------------+--------------------+
# |  50  | 0.0005628544309895833 | 0.0005581508574218749 |         0          |
# | 100  | 0.0025058136263020835 |   0.0022924026796875  | 4.451974592962666  |
# | 200  |   0.011205791196875   |  0.009884445343750001 | 4.471917256436895  |
# | 400  |  0.04224654831666667  |      0.0385922525     | 3.7700638513100366 |
# | 800  |  0.16669830331666666  |      0.158989744      | 3.945844334243576  |
# +------+-----------------------+-----------------------+--------------------+
# O(n^2) quadratic
def max_area_quadratic(height: List[int]):
    """O(n^2) brute force solution"""
    maxarea = 0
    for i, ele_i in enumerate(height):
        for j in range(i + 1, len(height)):
            maxarea = max(maxarea, min(ele_i, height[j]) * (j - i))
    return maxarea
