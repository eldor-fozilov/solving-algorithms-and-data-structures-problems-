# O(n) time | O(h) space - n is the number of nodes in the tree
# h is the hight of the tree

def invertBinaryTree(tree):
    if tree is None:
        return
    temp = tree.left
    tree.left = tree.right
    tree.right = temp
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
