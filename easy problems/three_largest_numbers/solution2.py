# Time Complexity: O(n), n is the number of elements in the array
# Auxiliary Space Complexity: O(1)


from math import inf
def findThreeLargestNumbers(array):
    
    output = [-inf]*3

    for num in array:
        for index in reversed(range(3)):
            if num > output[index]:
                for i in range(index):
                    temp = output[i] 
                    output[i] = output[i+1]
                    output[i+1] = temp
                output[index] = num
                break
    return output
