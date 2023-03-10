# O(h) time | O(1) space - h is the height of the tree

class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def findSuccessor(tree, node):
    if node.right is not None:
        current_node = node.right
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    current_node = node
    while current_node.parent is not None and current_node.parent.right is current_node:
        current_node = current_node.parent
    return current_node.parent

