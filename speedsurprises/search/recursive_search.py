"""Compute recursive search functions"""
# https://www.geeksforgeeks.org/exponential-search/


def compute_recursive_binary_search(list, x, left=0, right=None):
    if right is None:
        right = len(list) - 1
    if right >= left:
        mid = int(left + (right - left) / 2)
        # If the element is present at
        # the middle itself
        if list[mid] == x:
            return mid
        # If the element is smaller than mid,
        # then it can only be present in the
        # left subarray
        if list[mid] > x:
            return compute_recursive_binary_search(list, x, left, mid - 1)
        # Else he element can only be
        # present in the right
        return compute_recursive_binary_search(list, x, mid + 1, right)
    # We reach here if the element is not present
    return -1


# Returns the position of first
# occurrence of x in array
def compute_exponential_search(list, x):
    # IF x is present at first
    # location itself
    n = len(list) - 1
    if list[0] == x:
        return 0
    # Find range for binary search
    # j by repeated doubling
    i = 1
    while i < n and list[i] <= x:
        i = i * 2
    # Call binary search for the found range
    return compute_recursive_binary_search(list, x, i / 2, min(i, n))
