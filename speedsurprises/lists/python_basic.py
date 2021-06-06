"""Investigate the default list functions available in Python."""

# Reference:
# https://wiki.python.org/moin/TimeComplexity

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.lists.python_basic --function=list_copy --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=50 --max=1000

# Quit due to researched max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 3.2364913676578555e-07 |  3.22893491745517e-07  |         0          |
# | 100  | 4.911724624635274e-07  | 4.900162143706838e-07  | 1.5176078248556337 |
# | 200  | 6.632680439632061e-07  | 6.627776565548346e-07  | 1.3503770969498479 |
# | 400  | 1.1246698706308724e-06 | 1.1228371047961733e-06 | 1.6956491133066889 |
# | 800  | 2.7629981994630365e-06 | 2.758518898009904e-06  | 2.456719319699709  |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic


def list_copy(list):
    """Copy a list."""
    res = list.copy()
    return res

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.lists.python_basic --function=list_append --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=50 --max=1000

# Quit due to indicator:  0.004793372806200558
# +------+------------------------+------------------------+-------------------+
# | Size |          Mean          |         Median         |       Ratio       |
# +------+------------------------+------------------------+-------------------+
# |  50  | 2.5686807730998866e-07 | 2.5611526679970506e-07 |         0         |
# | 100  | 2.5934246689485414e-07 | 2.588452558517987e-07  | 1.009632919788158 |
# +------+------------------------+------------------------+-------------------+
# O(1) constant or O(logn) logarithmic


def list_append(list):
    # print(list)
    res = []
    res.append(list)
    return res


# NOTE: hypothesis will try generate empty list, which will cause error


def list_poplast(list):
    # print(list)
    list.pop()
    return list


# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.lists.python_basic --function=list_in --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=50 --max=1000


# Quit due to researched max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  50  | 6.812264496486193e-07  | 6.806814079277773e-07  |         0          |
# | 100  | 1.1444629109691924e-06 | 1.1440368995647987e-06 | 1.6800036339744489 |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic
# crash at 200


def list_in(list, x):
    res = 0
    if x in list:
        res = 1
    return res


def dict_in(dict, x):
    res = 0
    if x in dict:
        res = 1
    return res
