"""Sort list with InsertionSort"""

# Inspiration for function:
# https://bit.ly/2flYwOq

# Worst-case time complexity: O(n^2)

def insertionSort(list):
    for i in range(1, len(list)):
        currentValue = list[i]
        position = i
        while position > 0 and list[position - 1] > currentValue:
            list[position] = list[position - 1]
            position -= 1
        list[position] = currentValue
