""" Functions that create copies of characters and strings """

# Source and/or inspiration for these functions:
# http://whatcanbecomputed.com/


def mcopies_ofc(input_string):
    """Create M copies of the letter 'c'"""
    copy_count = int(input_string)
    list_of_letter_c = []
    # iterate M times, appending a single ``C'' character at each iteration
    for i in range(copy_count):
        list_of_letter_c.append("C")
    # join all the C's together into a single string, with no separator
    return "".join(list_of_letter_c)
