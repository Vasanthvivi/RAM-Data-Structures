class Node:
    def __init__(self, data):
        self.right=  None
        self.left = None
        self.data = data
        self.height = 1

class Tree:

    def createNode(self, data):
        return Node(data)

    def getHeight(self, node):


    def insert(self, node, data):
        if not node:
            return self.createNode(data)
        elif data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)

