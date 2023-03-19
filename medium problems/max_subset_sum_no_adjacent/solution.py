# O(n) time | O(1) space - n is the number of elements in the array

def maxSubsetSumNoAdjacent(array):

    if len(array) == 0:
        return 0
    elif len(array) <= 2:
        return max(array)
    
    max_sum_first = max(array[0], array[1])
    max_sum_second = array[0]
    max_sum = None
    for i in range(2, len(array)):
        max_sum = max(max_sum_first, max_sum_second + array[i])
        max_sum_second = max_sum_first
        max_sum_first = max_sum
    return max_sum
