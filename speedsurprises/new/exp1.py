"""Do embedded list iteration"""
import time

"""
+------+------------------------+------------------------+-------------------+
| Size |          Mean          |         Median         |       Ratio       |
+------+------------------------+------------------------+-------------------+
|  1   | 2.472663416031029e-06  | 2.4574149932732325e-06 |         0         |
|  2   | 0.00018298395102623506 | 0.0001816898613284934  | 74.00277362454366 |
|  4   |  0.055474572391297744  |  0.05534920849822811   | 303.1663273209362 |
|  8   |   8.307331772799564    |   8.303290908996132    | 149.7502624121665 |
+------+------------------------+------------------------+-------------------+
O(c^n) exponential

"""


def forloops(list):
    start_time = time.time()
    z = 0
    for a in range(len(list)):
        for b in range(len(list)):
            for c in range(len(list)):
                for d in range(len(list)):
                    for e in range(len(list)):
                        for f in range(len(list)):
                            for g in range(len(list)):
                                for e in range(len(list)):
                                    for h in range(len(list)):
                                        if (time.time() - start_time) < 3:
                                            z += 1
                                        else:
                                            break
    return z
