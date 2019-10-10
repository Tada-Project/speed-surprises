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


def compute_binary_search(list):
    """Search a list using linear search function."""
	first = 0
	last = len(list)-1
    # Search target set as the last number in the list for the worst case
    target = list[last]
	found = False
	while( first <= last and not found):
		mid = (first + last)//2
		if list[mid] == target :
			found = True
		else:
			if item < list[mid]:
				last = mid - 1
			else:
				first = mid + 1
	return found
