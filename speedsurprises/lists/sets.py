"""Represent and/or manipulate sets"""

# Source and/or inspiration for the function(s):
# https://is.gd/GIibZB

# Worst-case time complexity: O(len(list_one) * len(list_two)) -- Quadratic


def is_subset(first_list, second_list):
    """Assumes first_list and second_list are lists.
    Returns True if each element in list_one is also
    in list_two and False otherwise."""
    for element_one in first_list:
        matched = False
        for element_two in second_list:
            if element_one == element_two:
                matched = True
                break
        if not matched:
            return False
    return True
