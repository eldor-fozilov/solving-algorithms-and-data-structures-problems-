# O(n) time | O(n) space - where n is the number of nodes in the tree

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    if tree is None:
        return False
    stack = [tree.left, tree.right]
    while len(stack) != 0:
        start = 0
        end = len(stack) - 1
        while start < end:
            if stack[start] is None and stack[end] is not None:
                return False
            elif stack[start] is not None and stack[end] is None:
                return False
            elif stack[start] is None and stack[end] is None:
                pass
            elif stack[start].value != stack[end].value:
                return False
            start += 1
            end -= 1

        new_stack = []
        index = 0
        while index < len(stack):
            current_node = stack[index]
            if current_node is not None:
                new_stack.extend([current_node.left, current_node.right])
            index += 1
        stack = new_stack    
        
    return True
