from typing import List


def sort(array: List):
    print("Array: ", array)
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        sort(left)
        sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
        print("Sorted Array:", array)


array = [3, 5, 2, 3, 8, 1, 9, 4]
sort(array)
print("Sorted")
print(array)
