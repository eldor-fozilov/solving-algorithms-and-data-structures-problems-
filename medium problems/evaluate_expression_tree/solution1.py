# O(n) time | O(h) space - where n is the number of nodes in the tree,
# and h is the height of the tree

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def calculate(num1, num2, operator):
    if operator == -1:
        return num1 + num2
    elif operator == -2:
        return num1 - num2
    elif operator == -3:
        return int(num1 / num2)
    else:
        return num1 * num2

def evaluateExpressionTree(tree):

    if tree is None:
        return None

    operator = tree
    right_operand = tree.right
    left_operand = tree.left

    num1 = num2 = None

    if left_operand.value < 0:
        num1 = evaluateExpressionTree(left_operand)
    else:
        num1 = left_operand.value

    if right_operand.value < 0:
        num2 = evaluateExpressionTree(right_operand)
    else:
        num2 = right_operand.value

    return calculate(num1, num2, operator.value)
        
        
