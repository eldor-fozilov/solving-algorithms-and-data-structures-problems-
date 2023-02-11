# Time Complexity: O(n^2), n is the number of elements in the array
# Auxiliary Space Complexity: O(1)

def insertionSort(array):

    for i in range(len(array) - 1):
        for j in reversed(range(i + 1)):
            if array[j+1] < array[j]:
                swap(j,j+1, array)
            else:
                break

    return array
    
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]