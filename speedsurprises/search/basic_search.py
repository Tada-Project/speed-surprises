"""Compute basic search functions."""

# References:

# https://www.geeksforgeeks.org/python-program-for-linear-search/
# https://www.geeksforgeeks.org/python-program-for-binary-search/
# import random

import math


# Worst-case time complexity: O(n)

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.search.basic_search --function=compute_linear_search --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_and_intdiff.json --startsize=2 --max=1000

# Quit due to indicator:  0.072498847603935
# +------+-----------------------+----------------------+--------------------+
# | Size |          Mean         |        Median        |       Ratio        |
# +------+-----------------------+----------------------+--------------------+
# |  2   | 5.923778279622396e-07 | 5.86570930480957e-07 |         0          |
# |  4   | 6.849851735432942e-07 | 6.84989356994629e-07 | 1.1563315526167157 |
# +------+-----------------------+----------------------+--------------------+
# O(1) constant or O(logn) logarithmic

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.search.basic_search --function=compute_linear_search --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_and_intdiff.json --startsize=25 --max=1000

# Quit due to researched max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  25  | 1.8059576161702474e-06 | 1.7441474914550782e-06 |         0          |
# |  50  | 2.6361811065673826e-06 | 2.8011482238769534e-06 | 1.4597137180648376 |
# | 100  | 4.295276234944661e-06  |  5.18223876953125e-06  | 1.6293555189527988 |
# | 200  | 5.296670710245769e-06  | 3.2013801574707033e-06 | 1.2331385504741603 |
# | 400  | 2.2050148111979167e-05 | 2.069620361328125e-05  | 4.163020379825731  |
# | 800  | 3.6552219645182296e-05 | 3.533795166015624e-05  | 1.6576859012264231 |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic


def compute_linear_search(search_list, x):
    """Search a list using linear search function."""
    for i in range(len(search_list)):
        if search_list[i] == x:
            return i
    return -1


# Worst-case time complexity: O(logn)

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.search.basic_search --function=compute_iterative_binary_search --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_and_intdiff.json --startsize=25 --max=1000

# Quit due to indicator:  0.01750971078860441
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  25  | 1.8083479817708334e-06 | 1.9140090942382813e-06 |         0          |
# |  50  | 2.347823537190755e-06  | 2.2688491821289067e-06 | 1.2983250794969439 |
# | 100  | 2.2670189793904623e-06 | 2.562324142456055e-06  | 0.9655832065228471 |
# +------+------------------------+------------------------+--------------------+
# O(1) constant or O(logn) logarithmic


def compute_iterative_binary_search(search_list, target):
    """Search a list using linear search function."""
    first = 0
    last = len(search_list) - 1
    # Search target set as the last number in the list for the worst case
    # target = list[last]
    found = False
    while first <= last and not found:
        mid = int((first + last) / 2)
        if search_list[mid] == target:
            found = True
            return mid
        else:
            if target < search_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return -1


# O(n^(1/2))
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.search.basic_search --function=compute_jump_search --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_and_intdiff.json --startsize=25 --max=1000
# Quit due to researched max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  25  | 1.4621692403157552e-06 | 1.4651504516601558e-06 |         0          |
# |  50  | 2.0388897450764973e-06 |   1.998681640625e-06   | 1.394428010697448  |
# | 100  | 2.5746708424886067e-06 | 2.6229286193847656e-06 | 1.262780809362503  |
# | 200  | 4.873650614420573e-06  | 4.650808715820312e-06  | 1.892921818973114  |
# | 400  | 8.681521199544271e-06  | 8.267102050781251e-06  | 1.7813179249773559 |
# | 800  | 2.2384493204752603e-05 | 2.194199829101562e-05  | 2.5784067895759626 |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic


def compute_jump_search(search_list, x):
    """Search a list using jump search function."""
    n = len(search_list)
    step = int(math.floor(math.sqrt(n)))
    prev = 0
    while search_list[min(step, n) - 1] < x:
        prev = step
        step += int(math.floor(math.sqrt(n)))
        if prev >= n:
            return -1
    while search_list[prev] < x:
        prev = prev + 1
        if prev == min(step, n):
            return -1
    if search_list[prev] == x:
        return prev
    return -1


# O(n)
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.search.basic_search --function=compute_interpolation_search --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_and_intdiff.json --startsize=25 --max=1000
# Quit due to indicator:  0.02942966837610865
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  25  | 1.0009028879801433e-06 | 1.167576599121094e-06  |         0          |
# |  50  | 1.8570809682210286e-06 | 2.041374206542969e-06  | 1.8554057446758718 |
# | 100  | 1.969701919555664e-06  | 1.8561180114746092e-06 | 1.0606440716704557 |
# +------+------------------------+------------------------+--------------------+
# O(1) constant or O(logn) logarithmic
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.search.basic_search --function=compute_interpolation_search --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/list_and_intdiff.json --startsize=100 --max=1000
# Quit due to indicator:  0.018817638055081232
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# | 100  | 1.967643051147461e-06  | 1.9944023132324218e-06 |         0          |
# | 200  | 3.082644983927409e-06  | 2.801805877685546e-06  | 1.5666688031295706 |
# | 400  | 2.9687716166178388e-06 | 2.959245300292969e-06  | 0.9630598502573945 |
# +------+------------------------+------------------------+--------------------+
# O(1) constant or O(logn) logarithmic


def compute_interpolation_search(search_list, x):
    """Find indices of two corners."""
    lo = 0
    n = len(search_list)
    hi = n - 1
    # Since array is sorted, an element present
    # in array must be in range defined by corner
    while lo <= hi and x >= search_list[lo] and x <= search_list[hi]:
        if lo == hi:
            if search_list[lo] == x:
                return lo
            return -1
        # Probing the position with keeping
        # uniform distribution in mind.
        pos = lo + int(
            (
                (float(hi - lo) / (search_list[hi] - search_list[lo]))
                * (x - search_list[lo])
            )
        )
        # Condition of target found
        if search_list[pos] == x:
            return pos
        # If x is larger, x is in upper part
        if list[pos] < x:
            lo = pos + 1
        # If x is smaller, x is in lower part
        else:
            hi = pos - 1
    return -1
