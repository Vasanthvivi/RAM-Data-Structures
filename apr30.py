class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        self.height = 1


class TreeDriver(object):
    def createNode(self, data):
        return Node(data)


    # getting the height of the tree
    def getHeight(self, node):
        if not node:
            return 0
        else:
            return node.height

    def getBalanceFactor(self, node):
        if not node:
            return 0
        else:
            bf = self.getHeight(node.left) - self.getHeight(node.right)
            return bf

    def getSuccessor(self, node):
        if node is None or node.left is None:
            return node
        else:
            self.getSuccessor(node.left)

    def leftRotate(self, node):
        if node:
            root = node.right
            t = node.right.left
            node.right = t
            root.left = node
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
            root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
            return root

    def rightRotate(self, node):
        if node:
            root = node.left
            t = node.left.right
            node.left = t
            root.right = node
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
            root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
            return root

    # building the strands
    def buildNode(self, node, data):
        if not node:
            return self.createNode(data)
        elif data < node.data:
            node.left = self.buildNode(node.left, data)
        else:
            node.right = self.buildNode(node.right, data)
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        bf = self.getBalanceFactor(node)
        if bf < -1:
            if data > node.right.data:
                return self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)
        elif bf > 1:
            if data < node.left.data:
                return self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)
        return node


    # finding the data
    def find(self, node, data):
        if not node:
            print("not found")
            return node
        elif data < node.data:
            node.left = self.find(node.left, data)
        elif data > node.data:
            node.right = self.find(node.right, data)
        else:
            print("found ")
