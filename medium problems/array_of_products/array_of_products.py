# O(n) time | O(n) space - n is the number of elements in the array

def arrayOfProducts(array):

    total_product = 1
    count_zeros = 0
    output = []
    for num in array:
        
        if count_zeros > 1:
            total_product = 0
            break
        
        if num != 0:
            total_product *= num
        else:
            count_zeros += 1


    for i in range(len(array)):
        if array[i] != 0 and count_zeros != 0:
            output.append(0)
        elif array[i] != 0 and count_zeros == 0:
            output.append(total_product // array[i])
        else:
            output.append(total_product)

    return output
