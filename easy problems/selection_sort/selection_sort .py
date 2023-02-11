# Time Complexity: O(n^2), n is the number of elements in the array
# Auxiliary Space Complexity: O(1)

def selectionSort(array):

    for i in range(len(array)):
        min_num = array[i]
        min_index = i
        for j in range(i + 1, len(array)):
            if min_num > array[j]:
                min_num = array[j]
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    
    return array
