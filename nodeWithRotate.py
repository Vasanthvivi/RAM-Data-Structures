class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        self.height = 1

class Tree:
    def createNode(self, data):
        return Node(data)

    def insertNode(self, node, data):
        if node is None:
            return self.createNode(data)
        elif data < node.data:
            node.left = self.insertNode(node, data)

        else:
            node.right = self.insertNode(node, data)

    def getHeight(self, node):
        if not node:
            return 0
        else:
            return node.height

    def getBalanceFactor(self, node):
        if not node:
            return 0
        else:
            return (self.getHeight(node.left) - self.getHeight(node.right))

    def leftRotate(self, node):
        root = node.right
        node.right = root.left
        root.left = node
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        root.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))

    def rightRotate(self, node):
        root = node.left

