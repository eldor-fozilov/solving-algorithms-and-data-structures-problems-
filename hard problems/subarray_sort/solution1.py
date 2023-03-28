# O(n) time | O(1) space - where n is the length of the input array

def subarraySort(array):
    start = end = -1

    current_max = float("-inf")    
    for i in range(len(array) - 1):
        
        if array[i] > current_max:
            current_max = array[i]
        
        if array[i] > array[i+1]:
            current_min = array[i+1]
            j = i + 1
            for j in range(i+1, len(array)):
                if array[j] < current_max:
                    end = j
                else:
                    current_max = array[j]
                if array[j] < current_min:
                    current_min = array[j]
            
            k = i + 1
            while k >= 0:
                if array[k] <= current_min and k != i + 1:
                    start = k + 1
                    break
                elif k == 0:
                    start = 0
                k -= 1
        
        if start != -1 and end != -1:
            break
   
    return [start, end]
