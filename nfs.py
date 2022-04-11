class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.height = 1
        self.data = data


class MyTree(object):

    # utilities of node
    # building node in a ram
    def buildNode(self, data):
        return Node(data)

    # returning height of the tree
    def getHeight(self, node):
        if not node:
            return 0
        else:
            return node.height

    # getting the balance factor of the current node
    def getBalanceFactor(self, node):
        if not node:
            return 0
        else:
            bf = self.getHeight(node.left) - self.getHeight(node.right)
            return bf

    # leftrotate
    def leftRotate(self, node):
        root = node.right
        temp = root.left
        node.right = temp
        root.left = node
        node.height = max(self.getHeight(node.left) - self.getHeight(node.right))
        root.height = max(self.getHeight(root.left) - self.getHeight(node.right))
        return root

    # rightRotate
    def rightRotate(self, node):
        root = node.left
        temp = root.right
        node.left = temp
        root.right = node
        node.height = max(self.getHeight(node.left) - self.getHeight(node.right))
        root.height = max(self.getHeight(root.left) - self.getHeight(node.right))
        return root

    # finding successor to delete node
    def getSuccessor(self, node):
        if node is None or node.left is None:
            return node
        else:
            self.getSuccessor(node.left)

    # inserting a node
    def insert(self, node, data):
        if not node:
            return self.buildNode(data)
        elif data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        # updating the height of the node
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        # attain balance factor and do that
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

    # deleting a node
    def delete(self, node, data):
        if not node:
            return node
        elif data < node.data:
            node.left = self.deleteNode(node.left, data)

    # delete node
    def deleteNode(self, node, data):
        if data == node.data:
            print("deleting node")
            # check whether it got one child
            if node.right is None:
                t = node.left
                node = None
                return t
            elif node.left is None:
                t = node.right
                node = None
                return t
            temp = self.getSuccessor(node.right)
            node.data = temp.data
            node.right = self.deleteNode(node.right, node.key)
        elif not node:
            pass
        elif data < node.data:
            node.left = self.deleteNode(node.left, data)
        elif data > node.data:
            node.right = self.deleteNode(node.right, data)
        return node
