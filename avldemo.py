class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class Tree(object):
    # creating a node
    def createNode(self, data):
        return Node(data)

    # inserting data into the tree
    def insert(self, node, data):
        if not node:
            return self.createNode(data)
        elif data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        return node


    # getting the current node height
    def getHeight(self, node):
        if not node:
            return 0
        else:
            return node.height

    # getting the balance factor
    def getBalanceFactor(self, node):
        return ( self.getHeight(node.left) - self.getHeight(node.right) )

    # left rotate
    def leftRotate(self, node):
        root = node.right
        node.right = root.left
        root.left = node