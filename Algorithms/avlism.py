class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.height = 1

class AVLTree(object):

    # create a Node
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
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        print("node ",node.data," height is ",node.height)
        return node

    # get node height
    def getHeight(self, node):
        if not node:
            return 0
        else:
            return node.height

