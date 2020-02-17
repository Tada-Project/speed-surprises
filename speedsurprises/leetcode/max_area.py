"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms
a container, such that the container contains the most water.
https://leetcode.com/problems/container-with-most-water/
"""

from typing import List


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


def max_area_log(height: List[int]) -> int:
    """O(nlogn) solution"""
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


def max_area_quadratic(height: List[int]):
    """O(n^2) brute force solution"""
    maxarea = 0
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            maxarea = max(maxarea, min(height[i], height[j]) * (j - i))
    return maxarea
