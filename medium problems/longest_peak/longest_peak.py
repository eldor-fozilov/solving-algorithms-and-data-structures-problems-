# O(n) time | O(1) space - n is the number of elements in the array

def longestPeak(array):

    i = 0
    max_length = 0

    while i < len(array):
        left_side = i
        current_length = 0
        
        while left_side < len(array) - 1 and array[left_side] < array[left_side+1]:
            current_length += 1
            left_side += 1
        if current_length:
            right_side = left_side
            while right_side < len(array) - 1 and array[right_side] > array[right_side+1]:
                current_length += 1
                right_side += 1
            if right_side != left_side and current_length + 1 > max_length:
                max_length = current_length + 1
            i = right_side
        else:
            i += 1
    return max_length
