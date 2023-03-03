# O(n) | O(n + depth of the tree) => O(n) space - where n
# is the total number of nodes in the tree
# this is for each traversal method

def inOrderTraverse(tree, array):
    current_node = tree
    if current_node is not None:
        inOrderTraverse(current_node.left, array)
        array.append(current_node.value)
        inOrderTraverse(current_node.right, array)
    return array
    
def preOrderTraverse(tree, array):
    current_node = tree
    if current_node is not None:
        array.append(current_node.value)
        preOrderTraverse(current_node.left, array)
        preOrderTraverse(current_node.right, array)
    return array
    
def postOrderTraverse(tree, array):
    current_node = tree
    if current_node is not None:
        postOrderTraverse(current_node.left, array)
        postOrderTraverse(current_node.right, array)
        array.append(current_node.value)
    return array
