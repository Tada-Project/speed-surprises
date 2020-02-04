""" Compute the fibonacci function."""
import time

# Inspiration and source for the function:
# Previous works.
# https://www.programiz.com/python-programming/examples/fibonacci-recursion  (for recursive)


"""
+------+------------------------+------------------------+--------------------+
| Size |          Mean          |         Median         |       Ratio        |
+------+------------------------+------------------------+--------------------+
|  1   | 1.0043617251043191e-06 | 8.984589118798958e-07  |         0          |
|  2   |  8.22756351615735e-06  | 7.2899500422884955e-06 | 8.191832992543384  |
|  4   | 0.0011684514388055807  | 0.0010561002226268101  | 142.01670233368202 |
|  8   |   5.000030412267369    |   5.000030134498957    | 4279.194022285189  |
+------+------------------------+------------------------+--------------------+
O(c^n) exponential

"""


def compute_recursive_fibonacci(value):
    """ Assumes the value is a natural number. Returns the value!"""
    if value <= 1:
        return value
    else:
        return compute_recursive_fibonacci(value - 2) + compute_recursive_fibonacci(
            value - 1
        )


def compute_iterative_fibonacci(value):
    start_time = time.time()
    if value <= 1:
        return value
    else:
        x = 0
        y = 1
        for i in range(1, value):
            if (time.time() - start_time) < 5:
                z = x + y
                x = y
                y = z
            else:
                break
        return y
