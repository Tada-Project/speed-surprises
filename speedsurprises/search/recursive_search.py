"""Compute recursive search functions"""
# https://www.geeksforgeeks.org/exponential-search/


# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.search.recursive_search --function=compute_recursive_binary_search --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_and_intdiff.json --startsize=25 --max=1000
# Quit due to indicator:  0.09266699082185953
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  25  | 2.5416256459554037e-06 | 2.604081726074218e-06  |         0          |
# |  50  | 3.060784098307292e-06  | 3.0957870483398445e-06 | 1.2042623598711506 |
# +------+------------------------+------------------------+--------------------+
# O(1) constant or O(logn) logarithmic

# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.search.recursive_search --function=compute_recursive_binary_search --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_and_intdiff.json --startsize=200 --max=1000
# Quit due to indicator:  0.0014415027123466984
# +------+-----------------------+-----------------------+--------------------+
# | Size |          Mean         |         Median        |       Ratio        |
# +------+-----------------------+-----------------------+--------------------+
# | 200  | 3.773836161295573e-06 | 3.926867675781248e-06 |         0          |
# | 400  |  4.72131830851237e-06 | 4.544448852539062e-06 | 1.2510660523459298 |
# | 800  | 4.734949544270833e-06 |   4.591162109375e-06  | 1.0028871672841644 |
# +------+-----------------------+-----------------------+--------------------+
# O(1) constant or O(logn) logarithmic
# warning: didn't recognize array or object


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
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.search.recursive_search --function=compute_exponential_search --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_and_intdiff.json --startsize=25 --max=1000
# Quit due to indicator:  0.09106801036873877
# +------+------------------------+-----------------------+--------------------+
# | Size |          Mean          |         Median        |       Ratio        |
# +------+------------------------+-----------------------+--------------------+
# |  25  | 1.6770086924235027e-06 | 1.756690216064453e-06 |         0          |
# |  50  | 2.0130554962158204e-06 |  1.96852798461914e-06 | 1.2003846523339632 |
# +------+------------------------+-----------------------+--------------------+
# O(1) constant or O(logn) logarithmic

# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.search.recursive_search --function=compute_exponential_search --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_and_intdiff.json --startsize=200 --max=1000
# Quit due to indicator:  0.07090269021012043
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# | 200  | 4.174869283040364e-06  | 3.820034790039063e-06  |         0          |
# | 400  | 4.8120672607421875e-06 | 4.8517303466796874e-06 | 1.1526270487773889 |
# +------+------------------------+------------------------+--------------------+
# O(1) constant or O(logn) logarithmic


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
