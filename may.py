class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.height = 1
        self.data = data


class DriverTree(object):
    # build the node in ram
    def buildNode(self, data):
        return Node(data)

    # getting the height of the binary tree
    def getHeight(self, node):
        if not node:
            return 0
        else:
            return node.height

    # getting the balance factor of the taken node
    def getBalanceFactor(self, node):
        if not node:
            return 0
        else:
            bf = self.getHeight(node.left) - self.getHeight(node.right)
            return bf

    # getting the successor
    def getSuccessor(self, node):
        if node is None or node.left is None:
            return node
        else:
            return self.getSuccessor(node.left)

    # leftRotate
    def leftRotate(self, node):
        if node:
            root = node.right
            t = node.right.left
            node.right = t
            root.left = node
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
            root.height = 1 + max(self.getHeight(root.left), self.getHeight(node.left))
            return root

    # rightRotate
    def rightRotate(self, node):
        if node:
            root = node.right
            t = node.right.left
            node.right = t
            root.left = node
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
            root.height = 1 + max(self.getHeight(root.left), self.getHeight(node.left))
            return root

    # build the strands
    def buildStrand(self, node, data):
        if not node:
            return self.buildNode(data)
        elif data < node.data:
            node.left = self.buildStrand(node.left, data)
        else:
            node.right = self.buildStrand(node.right, data)
        # update height for each node while traversing
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        # getting the balance factor and update the height of the each tree strand
        bf = self.getBalanceFactor(node)
        # if violates the avl rules then rotate
        if bf < -1:
            # whether it is a right heavy only
            if data > node.right.data:
                return self.leftRotate(node)
            else:
                node.right = self.leftRotate(node.right)
                return self.leftRotate(node)
        elif bf > 1:
            if data < node.left.data:
                return self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)
        return node

    # finding a data
    def find(self, node, data):
        if not node:
            print("not found!")
            return 0
        elif data < node.data:
            self.find(node.left, data)
        elif data > node.data:
            self.find(node.right, data)
        else:
            print("found the data")
            return

    # deleting the node
    def deleteNode(self, node, data):
        if not node:
            print("not a node !")
            return -1
        elif data < node.data:
            self.deleteNode(node.left, data)
        elif data > node.data:
            self.deleteNode(node.right, data)
        else:
            print(f"data found to be deleted {data} at {node}")
            if node.left is None:
                t = node.right
                node = None
                return t
            elif node.right is None:
                t = node.left
                node = None
                return t
            t = self.getSuccessor(node.right)
            node.data = t.data
            node.right = self.deleteNode(node.right, t.data)
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        bf = self.getBalanceFactor(node)
        if bf < -1:
            if self.getBalanceFactor(node.right) <= 0:
                return self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node.right)
        elif bf > 1:
            if self.getBalanceFactor(node.left) > 1:
                return self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)
        return node