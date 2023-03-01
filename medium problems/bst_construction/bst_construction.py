
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(n)) time | O(log(n)) space
    # Worst: O(n) time | O(n) space 
    def insert(self, value):
        if value < self.value:
            if self.left is not None:
                self.left.insert(value)
            else:
                self.left = BST(value)
        else:
            if self.right is not None:
                self.right.insert(value)
            else:
                self.right = BST(value)
        return self
    
    # Average: O(log(n)) time | O(log(n)) space
    # Worst: O(n) time | O(n) space 
    def contains(self, value):
        if value < self.value:
            return self.left.contains(value) if self.left is not None else False
        elif value == self.value:
            return True
        else:
            return self.right.contains(value) if self.right is not None else False

    # Average: O(log(n)) time | O(log(n)) space
    # Worst: O(n) time | O(n) space 
    def remove(self, value, parent = None):

       current_node = self 
       if value < current_node.value:
           if current_node.left is not None:
               current_node.left.remove(value, parent = current_node)
       elif value > current_node.value:
            if current_node.right is not None:
                current_node.right.remove(value, parent = current_node)
       else:
            if current_node.left is not None and current_node.right is not None:
                current_node.value = current_node.right.get_min_value()
                current_node.right.remove(current_node.value, current_node) 

            elif parent is None:
                if current_node.left is not None:
                    current_node.value = current_node.left.value
                    current_node.right = current_node.left.right
                    current_node.left = current_node.left.left
                elif current_node.right is not None:
                    current_node.value = current_node.right.value
                    current_node.left = current_node.right.left
                    current_node.right = current_node.right.right
                else:
                    pass
            elif parent.left == current_node:
                parent.left = current_node.left if current_node.left is not None else current_node.right
            elif parent.right == current_node:
                parent.right = current_node.left if current_node.left is not None else current_node.right
                
       return self

    def get_min_value(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
