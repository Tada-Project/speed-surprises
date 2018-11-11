"""Functions that create copies of boolean and booleanlists"""

Boolean_T = True


def bcopies_oft(inputlength):
    """Create empty list for boolean true"""
    list_of_boolean_true = []
    # iterate length of booleanlist times, appending a boolean true at each iteration
    # pylint: disable=unused-variable
    for i in range(int(inputlength)):
        list_of_boolean_true.append(Boolean_T)
    # return copied list
    return list_of_boolean_true


def bcopies_of(booleanlist, boolean):
    """Create empty list for boolean true"""
    list_of_boolean_true = []
    # iterate length of booleanlist times, appending a boolean true at each iteration
    # pylint: disable=unused-variable
    for i in range(int(inputlength)):
        list_of_boolean_true.append(boolean)
    # return copied list
    return list_of_boolean_true
