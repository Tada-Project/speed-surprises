"""Compute basic search functions"""
# https://www.geeksforgeeks.org/python-program-for-linear-search/
# https://www.geeksforgeeks.org/python-program-for-binary-search/
# import random


# Worst-case time complexity: O(n)

def compute_linear_search(list):
    """Search a list using linear search function."""
    # x = random.choice(list)
    x = list[len(list) - 1]
    for i in range(len(list)):
        if list[i] == x:
            return i
    return -1
