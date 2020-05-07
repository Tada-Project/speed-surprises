"""Represent and/or manipulate sets"""

# Source and/or inspiration for the function(s):
# https://is.gd/GIibZB

# Worst-case time complexity: O(len(list_one) * len(list_two)) -- Quadratic
from functools import reduce
from constraint import *  # noqa: F403


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


# pipenv run python tada_a_bigoh.py --directory ../speed-surprises/ --module=speedsurprises.lists.sets --function=chinese_remainder --types hypothesis --schema=../speed-surprises/setjsonsch.json --expect="O(n)" --startsize=2 --maxsize=100
# Quit due to researched max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  2   | 2.4884350654602767e-06 | 2.2793624649044414e-06 |         0          |
# |  4   | 5.100421443685055e-06  | 4.838109588624698e-06  | 2.049650205657124  |
# |  8   | 8.036581383260438e-06  | 8.027064025882547e-06  | 1.5756700641298393 |
# |  16  | 1.457097603352724e-05  | 1.4547656188960978e-05 | 1.8130813761032059 |
# |  32  | 3.4191628263342357e-05 | 3.411936926270287e-05  | 2.3465571684881485 |
# |  64  | 7.879578753255216e-05  | 7.867523461918546e-05  | 2.3045345172119505 |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic
# https://medium.com/@fangya.123/chinese-remainder-theorem-with-python-a483de81fbb8
def chinese_remainder(n, a):
    # print(n)
    # print(a)
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    # print("prod", prod)
    for n_i, a_i in zip(n, a):
        # print("n_i", n_i)
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1 and b > 0:
        # print("a", a, "b", b)
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


# What is the number x ?
#
# x mod 3≡ 2
# x mod 5≡ 3
# x mod 7≡ 2
# if __name__ == '__main__':
#     n=[3,5,7]
#     a=[2,3,2]
#     print(chinese_remainder(n,a))


# Quit due to researched max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  2   |  1.59647088195806e-05  | 1.6025261047353245e-05 |         0          |
# |  4   | 3.5468029545080805e-05 | 3.531795446776176e-05  | 2.2216521419782818 |
# |  8   | 0.00010310213984373225 | 0.00010270925976563205 | 2.9069035175096687 |
# |  16  | 0.0003532465013020107  | 0.00035197851171853145 |  3.42618011456806  |
# |  32  |  0.001331467363281232  | 0.0013214952148441483  | 3.7692301505426213 |
# |  64  | 0.0052032496895833445  |  0.005203323656246539  | 3.9079062942711547 |
# +------+------------------------+------------------------+--------------------+
# O(n^2) quadratic


def CSP_basics_1(a, b):
    problem = Problem()  # noqa: F405
    problem.addVariable("a", a)
    problem.addVariable("b", b)
    return problem.getSolutions()


def CSP_basics_2(a, b):
    problem = Problem()
    problem.addVariable("a", a)
    problem.addVariable("b", b)
    problem.addConstraint(lambda a, b: a*2 == b, ("a", "b"))
    return problem.getSolutions()


# pipenv run python tada_a_bigoh.py --directory ../speed-surprises/ --module=speedsurprises.lists.sets --function=CSP_basics_3 --types hypothesis --schema=../speed-surprises/setjsonsch.json --expect="O(n)" --startsize=2 --maxsize=16
# Quit due to researched max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  2   | 2.0920423478190096e-05 | 2.0747366516114113e-05 |         0          |
# |  4   | 0.0002848394473958349  | 0.00028425626757810907 | 13.615376748600953 |
# |  8   |   0.7030071890166719   |   0.7036289069999953   | 2468.082266848801  |
# +------+------------------------+------------------------+--------------------+
# O(c^n) exponential
# freeze at size 16


def CSP_basics_3(a, b):
    problem = Problem()  # noqa: F405
    problem.addVariables(a, b)
    problem.addConstraint(AllDifferentConstraint())  # noqa: F405
    return problem.getSolutions()


# Quit due to researched max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  2   | 2.7639790193680533e-05 | 2.7573345703080232e-05 |         0          |
# |  4   | 0.0005505318202474759  | 0.0005508677363286196  | 19.918089695678933 |
# |  8   |   1.4531092024166734   |   1.4536827800000083   | 2639.4645122664656 |
# +------+------------------------+------------------------+--------------------+
# O(c^n) exponential


def CSP_rooks(cols, rows):
    problem = Problem()  # noqa: F405
    problem.addVariables(cols, rows)
    for col1 in cols:
        for col2 in cols:
            if col1 < col2:
                problem.addConstraint(lambda row1, row2: row1 != row2, (col1, col2))
    return problem.getSolutions()
