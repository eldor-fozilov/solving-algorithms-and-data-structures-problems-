# O(n) time | O(1) space - where n is the length of the input array

def isMonotonic(array):
    
    monotonically_inc_seq_len = 0
    monotonically_dec_seq_len = 0

    if len(array) <= 1:
        return True
    
    for i in range(len(array) - 1):
        if array[i+1] >= array[i]:
            monotonically_inc_seq_len += 1
        if array[i+1] <= array[i]:
            monotonically_dec_seq_len += 1
    
    if monotonically_inc_seq_len == (len(array) - 1) or monotonically_dec_seq_len == (len(array) - 1):
        return True
    
    return False
