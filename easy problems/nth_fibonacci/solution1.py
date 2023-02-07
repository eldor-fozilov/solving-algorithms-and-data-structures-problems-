# Time Complexity: O(2^n) - not optimal
# Space Complexity: O(n) - call stack will have at most n calls

def getNthFib(n):

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n-1) + getNthFib(n-2)