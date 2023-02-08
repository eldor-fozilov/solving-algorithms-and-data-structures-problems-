# Time Complexity: O(n), n is the number of elements in the array
# Auxialiry Space Complexity: O(d), d is the number of "special" sub-arrays in the array

def productSum(array, depth = 1, product_sum = 0):

    for num in array:
        if isinstance(num,int):
            product_sum += num
        else:
            product_sum += (depth + 1) * productSum(num, depth + 1)
    return product_sum
