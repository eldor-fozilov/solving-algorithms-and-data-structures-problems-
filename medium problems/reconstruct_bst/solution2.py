# O(n^2) time | O(n) space - n is the number of elements in the array

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    return _reconstructBst(0, len(preOrderTraversalValues) - 1, preOrderTraversalValues)

def _reconstructBst(left_idx, right_idx, values):
    if left_idx > right_idx:
        return None
    current_value = values[left_idx]
    temp_idx = left_idx + 1
    while temp_idx <= right_idx and values[temp_idx] < current_value:
        temp_idx += 1

    left_sub_tree = _reconstructBst(left_idx + 1, temp_idx - 1,values)
    right_sub_tree = _reconstructBst(temp_idx, right_idx, values)
    return BST(current_value, left_sub_tree, right_sub_tree)