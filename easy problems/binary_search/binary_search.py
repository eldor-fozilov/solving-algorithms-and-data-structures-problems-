# Time Complexity: O(log(n))
# Auxiliary Space Complexity: O(1)

def binarySearch(array, target):

    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if target > array[mid_index]:
            left_index = mid_index + 1
        elif target < array[mid_index]:
            right_index = mid_index - 1
        else:
            return mid_index

    return -1
