# O(n) time | O(n) space - where n is the number of nodes in the tree

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binaryTreeDiameter(tree):
    diameter = [float("-inf")]
    getTreeInfo(tree, diameter)
    return diameter[0]

def getTreeInfo(tree, maxDiameter):
    if tree is None:
        return 0

    leftTreeHeight = getTreeInfo(tree.left, maxDiameter)
    rightTreeHeight = getTreeInfo(tree.right, maxDiameter)

    longestPathThroughRoot = leftTreeHeight + rightTreeHeight
    maxDiameter[0] = max(longestPathThroughRoot, maxDiameter[0])
    currentHeight = 1 + max(leftTreeHeight, rightTreeHeight)

    return currentHeight

    
        
    
    
    


    
        
    
    
    
