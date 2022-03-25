class Node:
    def __init__(self, _data):
        self.left = None
        self.right = None
        self.data = _data
        self.height = 1

class Tree:
    # creating nodes
    def createNode(self, data):
        return Node(data)

    # inserting nodes
    def insert(self, node, data):
        if not node:
            return self.createNode(data)
        elif data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)

        return node