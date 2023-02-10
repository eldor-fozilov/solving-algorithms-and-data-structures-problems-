# Time Complexity: O(n), n is the number of elements in the array
# Auxiliary Space Complexity: O(1)

from math import inf

def findThreeLargestNumbers(array):

    output = [None]*3
    
    for iter in reversed(range(3)):
        max_num = -inf
        max_num_index = None
        for index, num in enumerate(array):
            if num > max_num and (num, index) not in output:
                max_num = num
                max_num_index = index
        output[iter] = (max_num, max_num_index)
    
    for i in range(len(output)):
        output[i] = output[i][0]
    
    return output
    