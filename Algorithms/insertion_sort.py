from typing import List


def sort(array: List) -> List:

    for i in range(1, len(array)):
        current = array[i]
        j = i-1
        while j >= 0 and array[j] > current:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = current
        print(array)
    return array


sorted = sort([3, 5, 2, 3, 8, 1, 9, 4])
print("Sorted")
print(sorted)
