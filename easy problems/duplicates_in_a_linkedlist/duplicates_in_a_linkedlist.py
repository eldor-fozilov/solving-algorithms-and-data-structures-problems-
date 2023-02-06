# Time Complexity: O(n), n is the number of nodes in the Linked List.
# Auxiliary Space Complexity: O(1)

# This is an input class.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):

    current_node = linkedList
    
    while current_node is not None:
        next_node = current_node.next 
        while (next_node is not None) and (current_node.value == next_node.value):
            next_node = next_node.next
        current_node.next = next_node
        current_node = current_node.next

    
    return linkedList
