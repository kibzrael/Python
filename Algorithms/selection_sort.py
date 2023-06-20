from typing import List


def swap(array: List, x: int, y: int) -> List:
    temp = array[x]
    array[x] = array[y]
    array[y] = temp
    return array


def minimum(array: List) -> List:
    min_value = 0
    min_index = 0
    for i in range(len(array)):
        val = array[i]
        if min_value == 0 or val < min_value:
            min_value = val
            min_index = i
    return min_index


def sort(array: List) -> List:
    for i in range(0, len(array)):
        min_index = minimum(array[i:])
        array = swap(array, i, min_index+i)
        print(array)
    return array


sorted = sort([3, 5, 2, 3, 8, 1, 9, 4])
print("Sorted")
print(sorted)
