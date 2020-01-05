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


# This function sorts array from left index to
# to right index which is of size atmost RUN
def tim_insertion_sort(arr, left, right):

    for i in range(left + 1, right + 1):

        temp = arr[i]
        j = i - 1
        while arr[j] > temp and j >= left:

            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = temp


# merge function merges the sorted runs
def tim_merge(arr, l, m, r):

    # original array is broken in two parts
    # left and right array
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l
    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:

        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # copy remaining elements of left, if any
    while i < len1:

        arr[k] = left[i]
        k += 1
        i += 1

    # copy remaining element of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


# iterative Timsort function to sort the
# array[0...n-1] (similar to merge sort)
def timSort(arr, n):

    RUN = 32
    # Sort individual subarrays of size RUN
    for i in range(0, n, RUN):
        tim_insertion_sort(arr, i, min((i + 31), (n - 1)))

    # start merging from size RUN (or 32). It will merge
    # to form size 64, then 128, 256 and so on ....
    size = RUN
    while size < n:

        # pick starting point of left sub array. We
        # are going to merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * size):

            # find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n - 1))

            # merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            tim_merge(arr, left, mid, right)

        size = 2 * size
