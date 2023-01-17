# Solution 1:

# Time Complexity: O(nlog(n))
# Space Complexity: O(n)

def sortedSquaredArray(array):

    for i in range(len(array)):
        array[i] = array[i]** 2
    array.sort()
    return array
    
# Solution 2:

# Time Complexity: O(n)
# Space Complexity: O(n)

def sortedSquaredArray(array):

    new_array = [0 for i in range(len(array))]
    start = 0
    end = len(array) - 1
    
    l = len(array) - 1
    counter = 0
    while start <= end:
        if abs(array[start]) > abs(array[end]):
            new_array[l - counter] = array[start]**2
            start += 1
        else:
            new_array[l - counter] = array[end]**2
            end -= 1
        counter += 1
    
    return new_array
    