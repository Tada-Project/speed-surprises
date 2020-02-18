"""Compute recursive search functions"""
# https://www.geeksforgeeks.org/exponential-search/


def compute_recursive_binary_search(list, l, r, x):
    if r >= l:
        mid = int(l + (r - l) / 2)
        # If the element is present at
        # the middle itself
        if list[mid] == x:
            return mid
        # If the element is smaller than mid,
        # then it can only be present in the
        # left subarray
        if list[mid] > x:
            return compute_recursive_binary_search(list, l,
                                                   mid - 1, x)
        # Else he element can only be
        # present in the right
        return compute_recursive_binary_search(list, mid + 1, r, x)
    # We reach here if the element is not present
    return -1


# Returns the position of first
# occurrence of x in array
def compute_exponential_search(list):
    # IF x is present at first
    # location itself
    n = len(list)
    x = list[len(list) - 1]
    if list[0] == x:
        return 0
    # Find range for binary search
    # j by repeated doubling
    i = 1
    while i < n and list[i] <= x:
        i = i * 2
    # Call binary search for the found range
    return compute_recursive_binary_search(list, i / 2,
                                           min(i, n), x)
