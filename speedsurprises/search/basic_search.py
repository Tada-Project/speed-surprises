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


# O(n)


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


# O(n)


def compute_interpolation_search(list, x):
    # Find indexs of two corners
    lo = 0
    n = len(list)
    hi = (n - 1)
    # Since array is sorted, an element present
    # in array must be in range defined by corner
    while lo <= hi and x >= list[lo] and x <= list[hi]:
        if lo == hi:
            if list[lo] == x:
                return lo;
            return -1;
        # Probing the position with keeping
        # uniform distribution in mind.
        pos  = lo + int(((float(hi - lo) /
            ( arr[hi] - list[lo])) * ( x - list[lo])))
        # Condition of target found
        if list[pos] == x:
            return pos
        # If x is larger, x is in upper part
        if list[pos] < x:
            lo = pos + 1;
        # If x is smaller, x is in lower part
        else:
            hi = pos - 1;
    return -1
