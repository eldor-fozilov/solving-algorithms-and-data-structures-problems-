# Time Complexity: O(V+E), V is the number of nodes, and E is the number of edges 
# Space Complexity: O(V), V is the number of nodes

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
    
    def depthFirstSearch(self, array):
        if self:
            array.append(self.name)

        for child_node in self.children:
            child_node.depthFirstSearch(array)
            
        return array