# O(n) time | O(h) space - where n is the number of nodes in the tree,
# and h is the height of the tree

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def evaluateExpressionTree(tree):

    if tree is None:
        return None

    if tree.value >= 0:
        return tree.value
    
    left_operand = evaluateExpressionTree(tree.left)
    right_operand = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return left_operand + right_operand
    elif tree.value == -2:
        return left_operand - right_operand
    elif tree.value == -3:
        return int(left_operand / right_operand)
    
    return left_operand * right_operand