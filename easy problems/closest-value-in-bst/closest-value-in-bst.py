# Time Complexity: On average, O(log(n))
# Space Complexity: On average, O(log(n))


def findClosestValueInBst(tree, target):

    d = {}
    current_node = tree # root node
    while current_node:
        node_value = current_node.value
        d[node_value] = abs(target - node_value)
        
        if target > node_value:
            current_node = current_node.right
        else:
            current_node = current_node.left

    return min(d, key = d.get)


# This is the class of the input tree.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
