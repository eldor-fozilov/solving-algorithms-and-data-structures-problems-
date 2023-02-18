# O(n) time | O(1) space - n is the length of the input array

def moveElementToEnd(array, toMove):

    left, right = 0, len(array) - 1

    while left < right:
        
        if array[left] == toMove:
            while array[right] == toMove and left != right:
                right -= 1
        
            # swaping operation
            array[left] = array[right]
            array[right] = toMove

        left += 1
    
    return array
