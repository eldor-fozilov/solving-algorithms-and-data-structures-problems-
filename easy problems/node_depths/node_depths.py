# Time Complexity: O(n), n is the number of nodes in a tree
# Space Complexity: on average O(log(n)), n is the number of node in a tree

def nodeDepth(node, depth):
    if node is None:
        return depth

    if node.left and node.right:
        return depth + nodeDepth(node.left, depth + 1) + nodeDepth(node.right, depth + 1)
    
    if node.left:
        return depth + nodeDepth(node.left, depth + 1)
    if node.right:
        return depth + nodeDepth(node.right, depth + 1)
    
    if node.left is None and node.right is None:
        return depth
        

def nodeDepths(root):
    return nodeDepth(root, 0)
    

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
