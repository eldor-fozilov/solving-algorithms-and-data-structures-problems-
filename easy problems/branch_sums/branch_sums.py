# Time Complexity: O(n), where n is the number of nodes in a tree
# Space Complexity: O(n) [the effect of keeping the list
# and call stack state after recursive calls] (n is the number of nodes in a tree)

# This is the class of the input root.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 

def branch_sum(node, sum_var, branch_sums):
    if node is None:
        branch_sums.append(sum_var)
    else:
        sum_var += node.value
        
        if node.left:
            branch_sum(node.left, sum_var, branch_sums)
        
        if node.right:
            branch_sum(node.right, sum_var, branch_sums)
        
        if node.left is None and node.right is None:
            branch_sum(None, sum_var, branch_sums)


def branchSums(root):

    branch_sums = []
    current_node = root
    branch_sum(root, 0, branch_sums)

    return branch_sums
