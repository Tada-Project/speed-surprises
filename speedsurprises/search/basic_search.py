"""Compute basic search functions"""
# https://www.geeksforgeeks.org/python-program-for-linear-search/
# https://www.geeksforgeeks.org/python-program-for-binary-search/
# import random
import math


# Worst-case time complexity: O(n)


def compute_linear_search(list):
    """Search a list using linear search function."""
    # x = random.choice(list)
    x = list[len(list) - 1]
    for i in range(len(list)):
        if list[i] == x:
            return i
    return -1


# Worst-case time complexity: O(logn)


def compute_iterative_binary_search(list):
    """Search a list using linear search function."""
    first = 0
    last = len(list) - 1
    # Search target set as the last number in the list for the worst case
    target = list[last]
    found = False
    while first <= last and not found:
        mid = (first + last) / 2
        if list[mid] == target:
            found = True
            return found
        else:
            if target < list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


def compute_jump_search(list):
    """Search a list using jump search function"""
    n = len(list)
    x = list[len(list) - 1]
    step = int(math.floor(math.sqrt(n)))
    prev = 0
    while list[min(step, n) - 1] < x:
        prev = step
        step += int(math.floor(math.sqrt(n)))
        if prev >= n:
            return -1
    while list[prev] < x:
        prev = prev + 1
        if prev == min(step, n):
            return -1
    if list[prev] == x:
        return prev
    return -1
