# O(n^2) time | O(n) space - n is the legth of the input array

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def insert(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BST(value)
        return self

def reconstructBst(preOrderTraversalValues):
    root_node = BST(preOrderTraversalValues[0])
    for idx in range(1,len(preOrderTraversalValues)):
        root_node.insert(preOrderTraversalValues[idx])
    return root_node

    