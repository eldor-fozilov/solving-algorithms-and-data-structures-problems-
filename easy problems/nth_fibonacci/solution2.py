# Time Complexity: O(n)
# Space Complexity: O(1)

def getNthFib(n):
    f_n_2 = 0
    f_n_1 = 1

    if n == 1:
        return 0
    elif n == 2:
        return 1
    
    result = 0

    for i in range(n-2):
        result = f_n_2 + f_n_1
        f_n_2 = f_n_1
        f_n_1 = result
        
    return result 
