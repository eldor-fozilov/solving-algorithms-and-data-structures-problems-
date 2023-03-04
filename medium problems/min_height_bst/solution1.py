# O(nlog(n)) time | O(n) space - where n is the length of the input array

def minHeightBst(array):
    left = 0
    right = len(array) - 1
    mid = (left + right) // 2
    min_height_tree = BST(array[mid]) # root
    _minHeightBst(array, min_height_tree, left, mid - 1)
    _minHeightBst(array, min_height_tree, mid + 1, right)
    
    return min_height_tree
    

def _minHeightBst(array, tree, left, right):
    mid = (left + right) // 2
    if left > right:
        return
    
    tree.insert(array[mid])
    _minHeightBst(array, tree, left, mid - 1)
    _minHeightBst(array, tree, mid + 1, right)
        

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)