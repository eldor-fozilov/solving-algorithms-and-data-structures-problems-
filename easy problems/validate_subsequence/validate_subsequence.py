# Solution 1

# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque
def isValidSubsequence(array, sequence):

    queue = deque(sequence)

    
    for num in array:
        if num == queue[0]:
            queue.popleft()
            if len(queue) == 0:
                return True
    return False
            
# Solution 2

# Time Complexity: O(n)
# Space Complexity: O(1)

def isValidSubsequence(array, sequence):

    index  = 0
    for num in array:
        if num == sequence[index]:
            index += 1

            if index == len(sequence):
                return True
    return False
