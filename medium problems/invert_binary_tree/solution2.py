# O(n) time | O(n) space - n is the number of nodes in the tree

def invertBinaryTree(tree):
    stack = [tree]

    while len(stack) != 0:
        current_node = stack.pop()
        if current_node is None:
            continue
        
        # swap operation
        temp = current_node.left
        current_node.left = current_node.right
        current_node.right = temp

        stack.extend([current_node.left, current_node.right])

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
