# Time Complexity: O(n^2), n is the number of elements in the array
# Auxiliary Space Complexity: O(1)

def bubbleSort(array):

    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                swap(i,i+1, array)
                isSorted = False
    
    return array

def swap(i,j, array):
    array[i], array[j] = array[j], array[i]
