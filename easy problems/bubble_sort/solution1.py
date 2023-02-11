# Time Complexity: O(n^2), n is the number of elements in the array
# Auxiliary Space Complexity: O(1)


def bubbleSort(array):

    while True:
        swap_num = 0
        count_iter = 1
        for i in range(len(array) - count_iter):
            prev = array[i]
            next = array[i+1]
            if prev > next:
                array[i] = next
                array[i+1] = prev
                swap_num += 1

        if swap_num == 0:
            return array
        count_iter += 1
