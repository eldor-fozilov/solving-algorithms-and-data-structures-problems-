# O(n) time | O(n) space - n is the number of elements in the array

def firstDuplicateValue(array):
    freq_set = set()
    for i in range(len(array)):
        if array[i] in freq_set:
            return array[i]
        else:
            freq_set.add(array[i])
    return -1
