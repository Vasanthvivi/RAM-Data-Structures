class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.height = 1
        self.data = data


class Tree:
    # build strand
    def buildStrand(self, data):
        return Node(data)

    # get height of the node
    def getHeight(self, node):
        if node is None:
            return 0
        else:
            return node.height

    # get the height of the strand nodes
    def getBalanceFactor(self, node):
        if node is None:
            return 0
        else:
            bf = self.getHeight(node.left) - self.getHeight(node.right)
            return bf

    # leftRotate
    def leftRotate(self, node):
        root = node.right
        t = root.left
        node.right = t
        root.left = node
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        return root

    # rightRotate
    def rightRotate(self, node):
        root = node.left
        t = root.right
        node.left = t
        root.right = node
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        return root

    # get the successor node
    def getSuccessor(self, node):
        if node is None or node.left is None:
            return node
        else:
            return self.getSuccessor(node.left)

    # inserting
    def insertData(self, node, data):
        if not node:
            return self.buildStrand(data)
        elif data < node.data:
            node.left = self.insertData(node.left, data)
        else:
            node.right = self.insertData(node.right, data)
        # update height of the each node while traverse backtracking
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        # according to the balance factor rotate
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
        else:
            pass
        return node


    def deleteData(self, node, data):
        if not node:
            return node
        elif data < node.data:
            node.left = self.deleteData(node.left, data)
        elif data > node.data:
            node.right = self.deleteData(node.right, data)
        else:
            print("value found at ", node, data)
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
            node.right = self.deleteData(node.right, node.data)
        # getting the height of the nodes and update the height while passing electricity
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        # according to the balance factor rotate
        bf = self.getBalanceFactor(node)
        if bf < -1:
            if self.getBalanceFactor(node.left) <= 0:
                return self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)
        elif bf > 1:
            if self.getBalanceFactor(node.right) >= 0:
                return self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)
        else:
            pass
        return node