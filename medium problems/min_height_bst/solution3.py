# O(n) time | O(n) space - where n is the length of the input array

def minHeightBst(array):
    return _minHeightBst(array, 0, len(array)- 1)
    
def _minHeightBst(array, left, right):
    if left > right:
        return None
    mid = (left + right) // 2
    tree = BST(array[mid])
    tree.left = _minHeightBst(array, left, mid - 1)
    tree.right = _minHeightBst(array, mid + 1, right)
    return tree

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None