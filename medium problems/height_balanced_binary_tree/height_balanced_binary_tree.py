# O(n) time | O(h) space - n is the number of nodes in the tree
# h is the height of the tree

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    check = check_balance(tree)
    if check:
        return True
    return False

def check_balance(tree):
    if tree is None:
        return 0
        
    height_left = check_balance(tree.left)
    if height_left is not False:
        height_right = check_balance(tree.right)

    if height_left is False or height_right is False:
        return False
    
    if abs(height_left - height_right) > 1:
        return False
    
    return max(height_left, height_right) + 1
