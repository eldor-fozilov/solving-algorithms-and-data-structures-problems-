# O(n^2) time | O(n) space, where n is the number of elements in the array

def threeNumberSum(array, targetSum):

    array.sort()
    result = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum < targetSum:
               left += 1
            elif current_sum > targetSum:
                right -= 1
            else:
                result.append([array[i], array[left], array[right]])
                left += 1
                right -= 1          
            
    return result
