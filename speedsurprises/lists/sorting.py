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
