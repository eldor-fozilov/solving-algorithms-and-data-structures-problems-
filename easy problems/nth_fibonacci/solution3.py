# Time Complexity: O(n)
# Space Complexity: O(n)

def getNthFib(n, memoize_dict = {1:0,2:1}): # fib index : fib value
    
    if n in memoize_dict:
        return memoize_dict[n]
    else:
        memoize_dict[n] = getNthFib(n-1, memoize_dict) + getNthFib(n-2, memoize_dict)
        return memoize_dict[n]