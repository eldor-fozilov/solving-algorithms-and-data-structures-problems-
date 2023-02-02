# Solution 1
# Time Complexity: O(nlog(n)), n is the number of queries
# Space Complexity: O(n) - input size

def minimumWaitingTime(queries):
    queries.sort() # O(nlog(n))
    total_wait_time = 0

    arr_len = len(queries)
        
    for i in range(arr_len):
        total_wait_time += queries[i] * (arr_len - (i+1)) 
    
    # [5,1,4,3,2] -> 5 + (5+1) + (5+1+4) + (5+1+4+3) =
    # = 5*4 + 1*3 + 4*2 + 3*1 + 2*0
    
    return total_wait_time


# Solution 2
# Time Complexity: O(nlog(n)), n is the number of queries
# Space Complexity: O(n) - input size

def minimumWaitingTime(queries):
    queries.sort() # O(nlog(n))
    total_wait_time = 0
    temp_sum = 0
    arr_len = len(queries)
        
    for i in range(arr_len - 1):
        temp_sum += queries[i]
        total_wait_time += temp_sum
        
    return total_wait_time