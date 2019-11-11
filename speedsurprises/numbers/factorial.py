"""Compute the numerical factorial function"""
import sys
import time

global TIME
TIME = 0
# Source and/or inspiration for the function(s):
# https://is.gd/GIibZB

# Worst-case time complexity: O(n) -- Linear


"""
+------+-----------------------+------------------------+--------------------+
| Size |          Mean         |         Median         |       Ratio        |
+------+-----------------------+------------------------+--------------------+
|  1   | 8.990552963254277e-07 | 7.307435302417176e-07  |         0          |
|  2   | 1.151414574177186e-05 | 1.0933244262822939e-05 | 12.806938337198925 |
|  4   |  0.006671919437576434 |  0.005236353812506422  | 579.4541416452249  |
|  8   |   5.0001012614329134  |   5.000087057997007    | 749.4247057709068  |
+------+-----------------------+------------------------+--------------------+
O(c^n) exponential
"""

def compute_iterative_factorial(value):
    """Assumes value is a natural number
    Returns value!"""
    global TIME
    TIME = time.time()
    if value < 0:
        ValueError("Inputs of 0 or grater!")
    result = 1
    while value != 0:
        if (time.time() - TIME) < 5:
            result *= value
            value -= 1
            print("in if", TIME, "value ", value)
        else:
            print("in else", TIME)
            break
    return result


def compute_recursive_factorial(value):
    start_time = time.time()
    if (time.time() - start_time) < 5:
        if value < 1:
            return 1
        else:
            return value * compute_recursive_factorial(value - 1)
    else:
        print("caused end", (time.time() - start_time))
        return 1


def compute_hashmap_recursive_factorial(value):
    dict = {0: 1}
    if value not in dict:
        dict[value] = value * compute_hashmap_recursive_factorial(value - 1)
    return dict[value]


def test(value):
    if value < 10:
        return 200
    else:
        sys.exit()
