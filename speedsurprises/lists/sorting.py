"""Do list sorting using InsertionSort"""

import math
import random
from heapq import heappush, heappop


# Inspiration for function:
# https://bit.ly/2flYwOq

# Worst-case time complexity: O(n^2)


def insertion_sort(list):
    for i in range(1, len(list)):
        currentValue = list[i]
        position = i
        while position > 0 and list[position - 1] > currentValue:
            list[position] = list[position - 1]
            position -= 1
        list[position] = currentValue
    return list


"""Do list sorting using BubbleSort"""

# Source and/or inspiration for the function(s):
# https://bit.ly/2pXGWai

# Worst-case time complexity: O(n^2)


def bubble_sort(list):
    """Sorts a list using BubbleSort function."""
    for num in range(len(list) - 1, 0, -1):
        for i in range(num):
            if list[i] > list[i + 1]:
                temp = list[i]
                list[i] = list[i + 1]
                list[i + 1] = temp
    return list


"""Do list sorting using MergeSort"""

# Source and/or inspiration for the function(s):
# https://bit.ly/2TOMWP3

# Worst-case time complexity: O(nlogn)


def merge_sort(list):
    """Sorts a list using MergeSort function."""
    if len(list) > 1:
        mid = len(list) // 2
        lefthalf = list[:mid]
        righthalf = list[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                list[k] = lefthalf[i]
                i = i + 1
            else:
                list[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            list[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            list[k] = righthalf[j]
            j = j + 1
            k = k + 1
    return list


# https://github.com/TheAlgorithms/Python/blob/master/sorts/tim_sort.py


def tim_binary_search(list, item, start, end):
    """Search used by tim_insertion_sort function."""
    if start == end:
        return start if list[start] > item else start + 1
    if start > end:
        return start
    mid = (start + end) // 2
    if list[mid] < item:
        return tim_binary_search(list, item, mid + 1, end)
    elif list[mid] > item:
        return tim_binary_search(list, item, start, mid - 1)
    else:
        return mid


def tim_insertion_sort(list):
    """Sorts a list using tim_insertion_sort function."""
    length = len(list)
    for index in range(1, length):
        value = list[index]
        pos = tim_binary_search(list, value, 0, index - 1)
        list = list[:pos] + [value] + list[pos:index] + list[index + 1 :]
    return list


def tim_merge(left, right):
    """Merge used by tim_sort_v1 function."""
    if not left:
        return right

    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + tim_merge(left[1:], right)

    return [right[0]] + tim_merge(left, right[1:])


def tim_sort_v1(list):
    """Sorts a list using tim_sort_v1 function."""
    length = len(list)
    runs, sorted_runs = [], []
    new_run = [list[0]]
    sorted_array = []
    i = 1
    while i < length:
        if list[i] < list[i - 1]:
            runs.append(new_run)
            new_run = [list[i]]
        else:
            new_run.append(list[i])
        i += 1
    runs.append(new_run)
    for run in runs:
        sorted_runs.append(tim_insertion_sort(run))
    for run in sorted_runs:
        sorted_array = tim_merge(sorted_array, run)
    return sorted_array


def python_sort(list):
    """Sorts a list using python default sort function."""
    list.sort()
    return list


# https://www.geeksforgeeks.org/timsort/


def time_merge_v2(list, low, mid, high):
    """merge used by tim_sort_v2 function."""
    len1, len2 = mid - low + 1, high - mid
    left, right = [], []
    for i in range(0, len1):
        left.append(list[low + i])
    for i in range(0, len2):
        right.append(list[mid + 1 + i])
    i, j, k = 0, 0, low
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            list[k] = left[i]
            i += 1
        else:
            list[k] = right[j]
            j += 1
        k += 1
    while i < len1:
        list[k] = left[i]
        k += 1
        i += 1
    while j < len2:
        list[k] = right[j]
        k += 1
        j += 1


def tim_sort_v2(list):
    n = len(list)
    for i in range(0, n, 32):
        list[i:i + 32] = insertion_sort(list[i : i + 32])
    size = 32
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n - 1))
            time_merge_v2(list, left, mid, right)
        size = 2 * size
    return list


# https://github.com/TheAlgorithms/Python/blob/master/sorts/wiggle_sort.py


def wiggle_sort(list):
    """nums[0] < nums[1] > nums[2] < nums[3]"""
    for i in range(len(list)):
        if (i % 2 == 1) == (list[i - 1] > list[i]):
            list[i - 1], list[i] = list[i], list[i - 1]
    return list


def heap_sort(list):
    """Sorts a list using heap_sort function."""
    h = []
    for value in list:
        heappush(h, value)
    list = []
    list = list + [heappop(h) for i in range(len(h))]
    return list


def partition(list, low, high):
    """partition used by quick_sort function."""
    pivot = list[high]
    i = low - 1
    for j in range(low, high):
        if list[j] <= pivot:
            i = i + 1
            (list[i], list[j]) = (list[j], list[i])
    (list[i + 1], list[high]) = (list[high], list[i + 1])
    return i + 1


def quick_sort(list, low=0, high=None):
    """Sorts a list using quick_sort function."""
    if high is None:
        high = len(list) - 1
    if low < high:
        pi = partition(list, low, high)
        quick_sort(list, low, pi - 1)
        quick_sort(list, pi + 1, high)
    return list


# https://github.com/endvroy/introSort/blob/master/quickSort.py


def random_partition(list, low, high):
    """partition used by random_quick_sort function."""
    index = random.randint(low, high)
    (list[low], list[index]) = (list[index], list[low])
    return partition(list, low, high)


def random_quick_sort(list, low=0, high=None):
    """Sorts a list using random_quick_sort function."""
    if high is None:
        high = len(list) - 1
    if low < high:
        pi = random_partition(list, low, high)
        quick_sort(list, low, pi - 1)
        quick_sort(list, pi + 1, high)
    return list


def intro_sort(list, low=0, high=None, depthlimit=0):
    """Sorts a list using intro_sort function."""
    if high is None:
        high = len(list) - 1

    if len(list) < 16:
        list = insertion_sort(list)

    if depthlimit < math.log2(len(list)):
        if low < high:
            mid = partition(list, low, high)
            intro_sort(list, low, mid - 1, depthlimit + 1)
            intro_sort(list, mid + 1, high, depthlimit + 1)
    else:
        list[low:high + 1] = heap_sort(list[low:high + 1])
    return list
