# Solution 1:

# Time Complexity: O(n^2)
# Space Complexity: O(1)

def twoNumberSum(array, targetSum):
    
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)) :
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []
    
# Solution 2:

# Time Complexity: O(n)
# Space Complexity: O(n)

def twoNumberSum(array, targetSum):

    d = {}
    for X in array:
        Y = targetSum - X
        if Y in d:
            return [X,Y]
        else:
            d[X] = Y
    return []
