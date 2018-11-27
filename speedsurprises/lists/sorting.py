"""Sort list with InsertionSort"""

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

        mergeSort(lefthalf)
        mergeSort(righthalf)

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
