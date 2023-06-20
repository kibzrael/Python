from typing import List


def sort(array: List) -> List:
    print("Array: ", array)
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        left_sorted = sort(left)
        right_sorted = sort(right)
        sorted_array = []
        i = j = 0
        while i < len(left_sorted) and j < len(right_sorted):
            if (left_sorted[i] <= right_sorted[j]):
                sorted_array.append(left_sorted[i])
                i += 1
            else:
                sorted_array.append(right_sorted[j])
                j += 1
        while i < len(left_sorted):
            sorted_array.append(left_sorted[i])
            i += 1
        while j < len(right_sorted):
            sorted_array.append(right_sorted[j])
            j += 1
        print("Sorted Array:", sorted_array)
        return sorted_array
    return array


sorted = sort([3, 5, 2, 3, 8, 1, 9, 4])
print("Sorted")
print(sorted)
