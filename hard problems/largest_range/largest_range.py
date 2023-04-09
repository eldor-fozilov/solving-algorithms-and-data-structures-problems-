# O(nlog(n)) time | O(1) space - where n is the length of the input array

def largestRange(array):

    array.sort()
    
    start_range_idx = 0
    end_range_idx = 0
    max_range = 0
    output = None
    identical_values = 0
    
    if len(array) == 1:
        return [array[0], array[0]]

    for i in range(len(array) - 1):
        
        if array[i+1] <= array[i] + 1:
            if array[i+1] == array[i]: identical_values += 1
            end_range_idx += 1
    
        if (array[i+1] > array[i] + 1) or end_range_idx == len(array) - 1:
            current_range = (array[end_range_idx] - array[start_range_idx]) + 1 - identical_values
            
            if current_range > max_range:
                max_range = current_range
                output = [array[start_range_idx], array[end_range_idx]]
            
            start_range_idx = end_range_idx = i + 1
            identical_values = 0
    
    if output is None:
        output = [array[0],array[-1]]
    
    return output
