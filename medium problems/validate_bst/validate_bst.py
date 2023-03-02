# O(n) time | O(d) space - n is the total number of nodes in the tree and d is
# the depth of the tree

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(tree, min_value, max_value):
    if tree is None:
        return True
    if tree.value < min_value or tree.value >= max_value:
        return False
    left_is_valid = validateBstHelper(tree.left, min_value, tree.value)
    right_is_valid = validateBstHelper(tree.right, tree.value, max_value)
    return left_is_valid and right_is_valid
    