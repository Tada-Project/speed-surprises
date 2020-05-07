"""Do list sorting using InsertionSort"""

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


def tim_binary_search(lst, item, start, end):
    """Search used by tim_insertion_sort function."""
    if start == end:
        return start if lst[start] > item else start + 1
    if start > end:
        return start

    mid = (start + end) // 2
    if lst[mid] < item:
        return tim_binary_search(lst, item, mid + 1, end)
    elif lst[mid] > item:
        return tim_binary_search(lst, item, start, mid - 1)
    else:
        return mid


def tim_insertion_sort(lst):
    """Sorts a list using tim_insertion_sort function."""
    length = len(lst)

    for index in range(1, length):
        value = lst[index]
        pos = tim_binary_search(lst, value, 0, index - 1)
        lst = lst[:pos] + [value] + lst[pos:index] + lst[index + 1 :]

    return lst


def tim_merge(left, right):
    """Merge used by tim_sort function."""
    if not left:
        return right

    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + tim_merge(left[1:], right)

    return [right[0]] + tim_merge(left, right[1:])


def tim_sort(lst):
    """Sorts a list using tim_sort function."""
    length = len(lst)
    runs, sorted_runs = [], []
    new_run = [lst[0]]
    sorted_array = []
    i = 1
    while i < length:
        if lst[i] < lst[i - 1]:
            runs.append(new_run)
            new_run = [lst[i]]
        else:
            new_run.append(lst[i])
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


# https://github.com/TheAlgorithms/Python/blob/master/sorts/wiggle_sort.py


def wiggle_sort(list):
    """nums[0] < nums[1] > nums[2] < nums[3]"""
    for i in range(len(list)):
        if (i % 2 == 1) == (list[i - 1] > list[i]):
            list[i - 1], list[i] = list[i], list[i - 1]
    return list
