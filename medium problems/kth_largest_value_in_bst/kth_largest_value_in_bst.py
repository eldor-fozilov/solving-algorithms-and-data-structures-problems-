# O(h + k) time | O(h) space - where h is the height of the tree

class BST:
        self.value = value
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right

def findKthLargestValueInBst(tree, k):
    return reverseInOrderTraversal(tree, k, count_target = [0, None])

def reverseInOrderTraversal(tree, k, count_target):
    if tree is not None:
        reverseInOrderTraversal(tree.right, k, count_target)
        count_target[0] += 1
        if count_target[0] == k:
            count_target[1] = tree.value
            return count_target[1]
        elif count_target[0] > k:
            return count_target[1]
        reverseInOrderTraversal(tree.left, k, count_target)
    return count_target[1]
            
    