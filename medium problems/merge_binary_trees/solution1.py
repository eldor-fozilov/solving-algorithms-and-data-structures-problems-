# O(n) time | O(h) space - n is the number of nodes in the smaller tree
# and h is the hight of the smaller tree

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def mergeBinaryTrees(tree1, tree2, parent_tree1 = None, parent_tree2 = None):
    
    if tree1 is None and parent_tree1 is None:
        return tree2
    elif tree1 is None and parent_tree1 is not None:
        if parent_tree2 is not None and tree2 is parent_tree2.left:
            parent_tree1.left = tree2
        elif parent_tree2 is not None and tree2 is parent_tree2.right:
            parent_tree1.right = tree2
        return tree1
    
    if tree2 is not None:
        tree1.value += tree2.value
        mergeBinaryTrees(tree1.left, tree2.left, tree1, tree2)
        mergeBinaryTrees(tree1.right, tree2.right, tree1, tree2)
    return tree1 
