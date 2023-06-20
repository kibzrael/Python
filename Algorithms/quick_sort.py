from typing import List


def sort(array: List) -> List:
    print("Array: ", array)
    pivot = array[len(array)-1]
    less = []
    more = []
    for i in range(len(array)-1):
        val = array[i]
        if (val < pivot):
            less.append(val)
        else:
            more.append(val)
    print("Less:", less, " Pivot:", pivot, " More:", more)
    if (len(less) > 1):
        less = sort(less)
    if (len(more) > 1):
        more = sort(more)
    array = [*less, pivot, *more]
    print("Less:", less, " Pivot:", pivot, " More:", more)
    print(array)
    return array


sorted = sort([3, 5, 2, 3, 8, 1, 9, 4])
print("Sorted")
print(sorted)
