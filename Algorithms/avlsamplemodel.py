class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class Tree:
    # Create Node
    def createNode(self, data):
        return Node(data)

    # insert via the root and appropriate data
    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        elif data < node.data:
            node.left = self.insert(node.left, data)
        elif data < node.data:
            node.right = self.insert(node.right, data)
        else:
            print("not sure how this happened")
