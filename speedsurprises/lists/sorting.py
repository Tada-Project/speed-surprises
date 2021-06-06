"""Perform list sorting using various sorting algorithms."""

import math
import random
from heapq import heappush, heappop


# Source and/or references for the function:
# https://bit.ly/2flYwOq

# Worst-case time complexity: O(n^2)
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.lists.sorting --function=insertion_sort --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=1 --max=1000

# Quit due to over maximum time: 209.21209025382996
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  1   | 4.524915059407552e-07  | 4.5213489532470694e-07 |         0          |
# |  2   |   6.926123046875e-07   | 6.956247329711916e-07  | 1.5306636601885382 |
# |  4   | 1.0413433202107747e-06 | 1.0345424652099606e-06 | 1.5035010397059272 |
# |  8   | 1.8795516459147136e-06 | 1.7844184875488283e-06 | 1.8049298530423954 |
# |  16  | 3.3020181274414063e-06 | 3.168002319335937e-06  | 1.756811596328563  |
# |  32  | 6.125781097412109e-06  |  5.94295654296875e-06  | 1.855162770459627  |
# |  64  | 1.181080790201823e-05  | 1.141099853515625e-05  | 1.9280492910541336 |
# | 128  | 2.4721272379557293e-05 | 2.2433477783203128e-05 | 2.0931059572421735 |
# | 256  | 5.179155883789062e-05  | 4.285797119140626e-05  | 2.0950199505393785 |
# | 512  | 9.924373697916667e-05  | 8.809033203125002e-05  | 1.9162145184662815 |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic
# might due to python under layer optimization


def insertion_sort(thelist):
    """Perform insertion sort."""
    for i in range(1, len(thelist)):
        currentValue = thelist[i]
        position = i
        while position > 0 and thelist[position - 1] > currentValue:
            thelist[position] = thelist[position - 1]
            position -= 1
        thelist[position] = currentValue
    return thelist


# Source and/or inspiration for the function(s):
# https://bit.ly/2pXGWai
#
# Worst-case time complexity: O(n^2)

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.lists.sorting --function=bubble_sort --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=1 --max=1000

# Quit due to end of rounds:  11
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  1   | 4.875064214070638e-07  | 4.781930923461915e-07  |         0          |
# |  2   | 9.349189503987631e-07  | 9.225513458251952e-07  | 1.9177572014340987 |
# |  4   | 1.924617131551107e-06  | 1.915631866455078e-06  | 2.0585924916060545 |
# |  8   | 5.508414713541667e-06  | 5.169726562500001e-06  | 2.862083384398782  |
# |  16  | 1.6641654866536458e-05 | 1.5801055908203126e-05 | 3.0211332537518056 |
# |  32  | 5.8059554036458334e-05 | 5.6653735351562494e-05 | 3.488808925679996  |
# |  64  | 0.00021507675130208334 | 0.0002162958007812501  | 3.7044161787227385 |
# | 128  | 0.0009774629036458332  | 0.0008446664062499998  | 4.544716701029904  |
# | 256  |  0.004020400208333334  | 0.0033850859375000007  | 4.113097482613065  |
# | 512  |  0.014749861666666668  |  0.013180387500000001  | 3.6687545772417662 |
# +------+------------------------+------------------------+--------------------+
# O(n^2) quadratic


def bubble_sort(thelist):
    """Sorts a list using BubbleSort function."""
    for num in range(len(thelist) - 1, 0, -1):
        for i in range(num):
            if thelist[i] > thelist[i + 1]:
                temp = thelist[i]
                thelist[i] = thelist[i + 1]
                thelist[i + 1] = temp
    return thelist


# Source and/or inspiration for the function(s):
# https://bit.ly/2TOMWP3

# Worst-case time complexity: O(nlogn)

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.lists.sorting --function=merge_sort --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=1 --max=1000

# Quit due to end of rounds:  11
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  1   |  2.86183926264445e-07  | 2.8064432144165035e-07 |         0          |
# |  2   | 1.723950932820638e-06  | 1.6791519165039063e-06 | 6.023926484353425  |
# |  4   | 5.411301269531249e-06  | 4.961297607421876e-06  | 3.138895177647291  |
# |  8   | 1.3783563232421875e-05 | 1.2650164794921872e-05 | 2.5471808989884366 |
# |  16  | 2.995317626953125e-05  | 2.9859680175781258e-05 | 2.1731083439349708 |
# |  32  |  6.82350146484375e-05  | 6.791970214843752e-05  | 2.278056057709213  |
# |  64  | 0.00015204205891927082 |  0.00015153408203125   | 2.2282117136286477 |
# | 128  | 0.00034780320963541665 | 0.00033261044921875004 | 2.2875460389554996 |
# | 256  | 0.0008022040690104167  | 0.0007409736328125001  |  2.30648840144783  |
# | 512  | 0.0016596982812499999  | 0.0015602148437500003  | 2.0689227908023096 |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic


def merge_sort(thelist):
    """Sorts a list using MergeSort function."""
    if len(thelist) > 1:
        mid = len(thelist) // 2
        lefthalf = thelist[:mid]
        righthalf = thelist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                thelist[k] = lefthalf[i]
                i = i + 1
            else:
                thelist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            thelist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            thelist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    return thelist


# Reference:
# https://github.com/TheAlgorithms/Python/blob/master/sorts/tim_sort.py


def tim_binary_search(thelist, item, start, end):
    """Search used by tim_insertion_sort function."""
    if start == end:
        return start if thelist[start] > item else start + 1
    if start > end:
        return start
    mid = (start + end) // 2
    if thelist[mid] < item:
        return tim_binary_search(thelist, item, mid + 1, end)
    elif thelist[mid] > item:
        return tim_binary_search(thelist, item, start, mid - 1)
    else:
        return mid


def tim_insertion_sort(thelist):
    """Sorts a list using tim_insertion_sort function."""
    length = len(thelist)
    for index in range(1, length):
        value = thelist[index]
        pos = tim_binary_search(thelist, value, 0, index - 1)
        thelist = thelist[:pos] + [value] + thelist[pos:index] + thelist[index + 1 :]
    return thelist


def tim_merge(left, right):
    """Merge used by tim_sort_v1 function."""
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + tim_merge(left[1:], right)
    return [right[0]] + tim_merge(left, right[1:])


# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.lists.sorting --function=tim_sort_v1 --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=1 --max=1000

# Quit due to end of rounds:  11
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  1   | 1.4470693715413411e-06 | 1.6252517700195314e-06 |         0          |
# |  2   | 2.5921161142985024e-06 | 2.2212371826171876e-06 |  1.79128669659943  |
# |  4   | 6.175288899739584e-06  | 6.5448608398437496e-06 | 2.3823349832500793 |
# |  8   | 1.5856283772786457e-05 | 1.5995996093750006e-05 | 2.5676991036735344 |
# |  16  | 3.608486206054688e-05  | 3.382388916015625e-05  | 2.275745223636699  |
# |  32  | 0.00013178459309895834 |   0.0001312279296875   | 3.6520741821830067 |
# |  64  |  0.000419993232421875  | 0.00038749384765624986 | 3.186967630628096  |
# | 128  | 0.0016828628645833333  | 0.0016557820312499997  | 4.006880908245042  |
# | 256  |  0.008654281666666666  |  0.008519262500000003  | 5.142594710953714  |
# | 512  |  0.07012807083333333   |  0.06902977499999999   |  8.10328038009702  |
# +------+------------------------+------------------------+--------------------+
# O(n^3) cubic


def tim_sort_v1(thelist):
    """Sorts a list using tim_sort_v1 function."""
    length = len(thelist)
    runs, sorted_runs = [], []
    new_run = [thelist[0]]
    sorted_array = []
    i = 1
    while i < length:
        if thelist[i] < thelist[i - 1]:
            runs.append(new_run)
            new_run = [thelist[i]]
        else:
            new_run.append(thelist[i])
        i += 1
    runs.append(new_run)
    for run in runs:
        sorted_runs.append(tim_insertion_sort(run))
    for run in sorted_runs:
        sorted_array = tim_merge(sorted_array, run)
    return sorted_array


# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.lists.sorting --function=python_sort --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=1 --max=1000

# Quit due to indicator:  0.011003815565909915
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  1   | 3.281067752838135e-07  | 3.6464576721191406e-07 |         0          |
# |  2   | 3.3540796915690105e-07 | 3.045936584472656e-07  | 1.0222524934657993 |
# +------+------------------------+------------------------+--------------------+
# O(1) constant or O(logn) logarithmic

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.lists.sorting --function=python_sort --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=25 --max=1000

# Quit due to researched max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  25  | 5.575285212198893e-07  | 5.438032150268554e-07  |         0          |
# |  50  | 7.831215159098307e-07  | 7.808071136474608e-07  | 1.404630411008099  |
# | 100  | 1.2665103276570637e-06 |  1.2513427734375e-06   | 1.617259010162212  |
# | 200  |  2.25087163289388e-06  | 2.253810119628906e-06  |  1.77722327543732  |
# | 400  | 4.246191965738932e-06  | 4.2160263061523426e-06 | 1.8864656267757598 |
# | 800  | 8.159199930826822e-06  | 8.131915283203127e-06  | 1.9215334578984207 |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic


def python_sort(thelist):
    """Sorts a list using python def1ault sort function."""
    thelist.sort()
    return thelist


# Reference:
# https://www.geeksforgeeks.org/timsort/


# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.lists.sorting --function=tim_sort_v2 --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=1 --max=1000

# Quit due to over maximum time: 205.19060397148132
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  1   | 1.3753764216105144e-06 | 1.5277198791503905e-06 |         0          |
# |  2   |  1.68765567779541e-06  | 1.723809814453125e-06  | 1.2270500288344541 |
# |  4   | 2.2010249328613283e-06 | 2.514012908935547e-06  | 1.3041907551524574 |
# |  8   | 2.9334097290039063e-06 | 2.6106002807617183e-06 | 1.3327471602924912 |
# |  16  | 4.952356262207031e-06  | 4.149343872070313e-06  | 1.6882593022177967 |
# |  32  | 8.863065795898438e-06  | 9.581607055664063e-06  | 1.7896664388899575 |
# |  64  | 4.489340861002604e-05  | 5.0427441406249995e-05 | 5.065223438914486  |
# | 128  | 0.0001131572021484375  |  0.000104332275390625  | 2.5205749719607193 |
# | 256  | 0.00031722657552083334 |   0.0002804115234375   | 2.8034148025743995 |
# | 512  |  0.00083103263671875   | 0.0007166007812500002  | 2.6196816434888297 |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic


def time_merge_v2(thelist, low, mid, high):
    """merge used by tim_sort_v2 function."""
    len1, len2 = mid - low + 1, high - mid
    left, right = [], []
    for i in range(0, len1):
        left.append(thelist[low + i])
    for i in range(0, len2):
        right.append(thelist[mid + 1 + i])
    i, j, k = 0, 0, low
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            thelist[k] = left[i]
            i += 1
        else:
            thelist[k] = right[j]
            j += 1
        k += 1
    while i < len1:
        thelist[k] = left[i]
        k += 1
        i += 1
    while j < len2:
        thelist[k] = right[j]
        k += 1
        j += 1


def tim_sort_v2(thelist):
    n = len(thelist)
    for i in range(0, n, 32):
        thelist[i : i + 32] = insertion_sort(thelist[i : i + 32])
    size = 32
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n - 1))
            time_merge_v2(thelist, left, mid, right)
        size = 2 * size
    return thelist


# Reference:
# https://github.com/TheAlgorithms/Python/blob/master/sorts/wiggle_sort.py

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.lists.sorting --function=wiggle_sort --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=25 --max=1000

# Quit due to researched max size
# +------+-----------------------+------------------------+--------------------+
# | Size |          Mean         |         Median         |       Ratio        |
# +------+-----------------------+------------------------+--------------------+
# |  25  | 4.532192484537761e-06 | 4.319052124023438e-06  |         0          |
# |  50  |  8.35620107014974e-06 |  8.24366760253906e-06  | 1.8437436403370213 |
# | 100  | 1.813418436686198e-05 | 1.5804437255859375e-05 | 2.170146962073643  |
# | 200  | 3.573169067382812e-05 | 3.1512463378906256e-05 | 1.9704051724059588 |
# | 400  | 7.004961263020833e-05 |    6.4394140625e-05    | 1.960433758078975  |
# | 800  |  0.000132110244140625 |  0.000130096142578125  | 1.885952529645446  |
# +------+-----------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic


def wiggle_sort(thelist):
    """Calculate nums[0] < nums[1] > nums[2] < nums[3]."""
    for i in range(len(thelist)):
        if (i % 2 == 1) == (thelist[i - 1] > thelist[i]):
            thelist[i - 1], thelist[i] = thelist[i], thelist[i - 1]
    return thelist


# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.lists.sorting --function=heap_sort --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=2 --max=1000

# Quit due to over maximum time: 202.94003653526306
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  2   | 1.2339463678995768e-06 | 1.234913635253906e-06  |         0          |
# |  4   | 1.7370465850830077e-06 | 1.703450012207032e-06  | 1.4077164374978532 |
# |  8   | 2.833589350382487e-06  | 2.7881660461425782e-06 | 1.631268484516251  |
# |  16  | 5.051138814290365e-06  | 5.053131103515626e-06  | 1.7825938023124437 |
# |  32  | 9.992328084309896e-06  | 9.738980102539066e-06  | 1.9782327217062872 |
# |  64  | 1.9487992350260418e-05 | 1.907093505859375e-05  | 1.9502954852794272 |
# | 128  | 4.2744158528645834e-05 |  4.13659423828125e-05  |  2.19335874934673  |
# | 256  | 9.218006673177083e-05  |  8.61071533203125e-05  | 2.156553548012755  |
# | 512  |  0.000194287646484375  | 0.00018417753906249998 | 2.1076969606641835 |
# | 1024 | 0.00041344592773437497 |   0.0003920462890625   | 2.1280093470462886 |
# +------+------------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic


def heap_sort(thelist):
    """Sorts a list using heap_sort function."""
    h = []
    for value in thelist:
        heappush(h, value)
    thelist = []
    thelist = thelist + [heappop(h) for i in range(len(h))]
    return thelist


def partition(thelist, low, high):
    """partition used by quick_sort function."""
    pivot = thelist[high]
    i = low - 1
    for j in range(low, high):
        if thelist[j] <= pivot:
            i = i + 1
            (thelist[i], thelist[j]) = (thelist[j], thelist[i])
    (thelist[i + 1], thelist[high]) = (thelist[high], thelist[i + 1])
    return i + 1


# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.lists.sorting --function=quick_sort --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=2 --max=1000

# Quit due to researched max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  2   | 1.6320862325032553e-06 |  1.53879623413086e-06  |         0          |
# |  4   | 4.728462575276693e-06  | 4.666320800781251e-06  | 2.8971891810056434 |
# |  8   | 1.3877457275390626e-05 | 1.3275958251953126e-05 | 2.9348772575573503 |
# |  16  | 4.057427286783854e-05  | 3.9027136230468764e-05 | 2.9237541188320066 |
# |  32  | 0.00014406861002604166 | 0.00012898266601562498 | 3.550737939169295  |
# |  64  |  0.00046006423828125   | 0.0004505166015625001  | 3.1933690357537934 |
# | 128  |    0.0018266690625     | 0.0017196640624999996  | 3.970465231821185  |
# | 256  |  0.007925843229166667  |  0.006917471875000003  | 4.338959580516061  |
# | 512  |  0.029972386666666666  |  0.027319300000000005  | 3.781602259854186  |
# +------+------------------------+------------------------+--------------------+
# O(n^2) quadratic
# crashed at 1024


def quick_sort(thelist, low=0, high=None):
    """Sorts a list using quick_sort function."""
    if high is None:
        high = len(thelist) - 1
    if low < high:
        pi = partition(thelist, low, high)
        quick_sort(thelist, low, pi - 1)
        quick_sort(thelist, pi + 1, high)
    return thelist


# Reference:
# https://github.com/endvroy/introSort/blob/master/quickSort.py


def random_partition(thelist, low, high):
    """partition used by random_quick_sort function."""
    index = random.randint(low, high)
    (thelist[low], thelist[index]) = (thelist[index], thelist[low])
    return partition(thelist, low, high)


# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.lists.sorting --function=random_quick_sort --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=2 --max=1000

# Quit due to researched max size
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  2   | 3.334341786702474e-06  | 3.2480255126953135e-06 |         0          |
# |  4   | 6.331579895019531e-06  | 6.239465332031248e-06  | 1.8988994830314627 |
# |  8   | 1.4764509887695313e-05 | 1.4449200439453121e-05 | 2.3318840056506573 |
# |  16  | 4.0509077148437495e-05 | 4.037988281250001e-05  | 2.7436790964661553 |
# |  32  | 0.00013009978678385416 |  0.00013099287109375   | 3.211620603133694  |
# |  64  | 0.0004959512565104166  | 0.0004668039062500002  | 3.8120835457969093 |
# | 128  |   0.001881130234375    | 0.0017501820312500003  | 3.7929740265422436 |
# | 256  |  0.007214183854166667  |  0.006638784374999998  | 3.8350262636459926 |
# | 512  |     0.03046913125      |  0.027009112499999995  | 4.223503568238293  |
# +------+------------------------+------------------------+--------------------+
# O(n^2) quadratic


def random_quick_sort(thelist, low=0, high=None):
    """Sorts a list using random_quick_sort function."""
    if high is None:
        high = len(thelist) - 1
    if low < high:
        pi = random_partition(thelist, low, high)
        quick_sort(thelist, low, pi - 1)
        quick_sort(thelist, pi + 1, high)
    return thelist


# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.lists.sorting --function=intro_sort --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=1 --max=1000

# Quit due to indicator:  0.02063312599387209
# +------+------------------------+------------------------+--------------------+
# | Size |          Mean          |         Median         |       Ratio        |
# +------+------------------------+------------------------+--------------------+
# |  2   | 6.6363053385416665e-06 | 6.321441650390624e-06  |         0          |
# |  4   | 1.2832618204752604e-05 | 1.2099975585937502e-05 | 1.9336991820169296 |
# |  8   | 2.3992188720703124e-05 |  2.3658154296875e-05   | 1.869625382590868  |
# |  16  | 2.302213623046875e-05  | 2.2438531494140624e-05 | 0.9595679868340938 |
# +------+------------------------+------------------------+--------------------+
# O(1) constant or O(logn) logarithmic

# pylint: disable=line-too-long
# pipenv run python tada_a_bigoh.py --directory ../speed_surprises/ --module=speedsurprises.lists.sorting --function=intro_sort --types hypothesis --schema=../speed_surprises/speedsurprises/jsonschema/single_int_list.json --startsize=25 --max=1000

# Quit due to researched max size
# +------+-----------------------+------------------------+--------------------+
# | Size |          Mean         |         Median         |       Ratio        |
# +------+-----------------------+------------------------+--------------------+
# |  25  | 3.707258056640625e-05 | 3.6930664062499997e-05 |         0          |
# |  50  | 8.031991129557291e-05 | 7.724047851562503e-05  | 2.1665584124013137 |
# | 100  |  0.00017802876953125  |    0.0001681765625     | 2.216496092433591  |
# | 200  |   0.000383940703125   |   0.0003749341796875   | 2.1566216748894935 |
# | 400  | 0.0009074698177083334 | 0.0008736660156249999  | 2.3635676299027026 |
# | 800  | 0.0020496763541666668 | 0.0019784421875000003  | 2.2586716540532326 |
# +------+-----------------------+------------------------+--------------------+
# O(n) linear or O(nlogn) linearithmic


def intro_sort(thelist, low=0, high=None, depthlimit=0):
    """Sorts a list using intro_sort function."""
    if high is None:
        high = len(thelist) - 1

    if len(thelist) < 16:
        thelist = insertion_sort(thelist)

    if depthlimit < math.log2(len(thelist)):
        if low < high:
            mid = partition(thelist, low, high)
            intro_sort(thelist, low, mid - 1, depthlimit + 1)
            intro_sort(thelist, mid + 1, high, depthlimit + 1)
    else:
        thelist[low : high + 1] = heap_sort(thelist[low : high + 1])
    return thelist
