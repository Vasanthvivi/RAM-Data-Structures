class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.height = 1
        self.data = data


class Tree:
    # build the node
    def buildNode(self, data):
        return Node(data)

    # get the height of the node
    def getHeight(self, node):
        if node is None:
            return 0
        else:
            return node.height

    # get the balance factor of the node
    def getBalanceFactor(self, node):
        if node is None:
            return 0
        else:
            bf = self.getHeight(node.left) - self.getHeight(node.right)
            return bf

    # left rotation
    def leftRotate(self, node):
        if node:
            root = node.right
            node.right = root.left
            root.left = node
            node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
            root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
            return root

    # right rotation
    def rightRotate(self, node):
        if node:
            root = node.right
            node.left = root.right
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

    # inserting function
    def insertNode(self, node, data):
        if node is None:
            return self.buildNode(data)
        elif data < node.data:
            node.left = self.insertNode(node.left, data)
        elif data > node.data:
            node.right = self.insertNode(node.right, data)
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        bf = self.getBalanceFactor(node)
        if bf < -1:
            if data > node.right.data:
                return self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node.right)
        elif bf > 1:
            if data < node.left.data:
                return self.rightRotate(node)
            else:
                node.left = self.rightRotate(node.left)
                return self.rightRotate(node)
        else:
            pass
        return node

    # deleting the node from the branch
    def deleteNode(self, node, data):
        if not node:
            return -1
        elif data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        else:
            print("deleting the appropriate value here")
            # if the node is a last leaf
            if node.left is None:
                t = node.right
                node = None
                return t
            if node.right is None:
                t = node.left
                node = None
                return node
            # if the node is in the middle of the branches rather than the leaves
            t = self.getSuccessor(node.right)
            node.data = t.data
            node.right = self.deleteNode(node.right, node.data)
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        bf = self.getBalanceFactor(node)
        if bf < -1:
            if self.getBalanceFactor(node.right) <= 0:
                return self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node.right)
        elif bf > 1:
            if self.getBalanceFactor(node.left) >= 0:
                return self.rightRotate(node)
            else:
                node.left = self.rightRotate(node.left)
                return self.rightRotate(node)
        return node

    # ascending sorted
    def inorder(self, root):
        if not root:
            pass
        else:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    # descending order
    def descendingSorted(self, root):
        if not root:
            pass
        else:
            self.descendingSorted(root.right)
            print(root.data)
            self.descendingSorted(root.left)

