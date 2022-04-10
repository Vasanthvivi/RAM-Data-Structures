class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        self.height = 1

class Tree:
    def buildNode(self, data):
        return Node(data)

    def getHeight(self, node):
        if not node:
            return 0
        else:
            return node.height

    def getBalanceFactor(self, node):
        if not node:
            return 0
        else:
            factor = self.getHeight(node.left) - self.getHeight(node.right)
            return factor

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y

    def insert(self, node, data):
        if not node:
            return self.buildNode(data)
        elif data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        # height of the node to be updated is
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        bf = self.getBalanceFactor(node)
        # rotate either right or left accordingly
        if bf < -1:
            print("rotating")
            if data > node.right.data:
                return self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)
        elif bf > 1:
            print("rotating")
            if data < node.left.data:
                return self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)
        else:
            print("no need rotation")
        return node


