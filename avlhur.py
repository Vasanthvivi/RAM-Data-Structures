
# build a node model to be in RAM
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.height = 1


class AVL(object):

    # build a node
    def buildNode(self, data):
        return Node(data)


    def getNodeHeight(self, node):
        if node is None:
            return 0
        else:
            return node.height


    def getBalanceFactor(self, node):
        if node is None:
            return 0
        else:
            bf = self.getNodeHeight(node.left) - self.getNodeHeight(node.right)
            return bf

    def getSuccessor(self, node):
        if node is None or node.left is None:
            return node
        return self.getSuccessor(node.left)


    def leftRotate(self, node):
        root = node.right
        t = root.left
        node.right = t
        root.left = node
        node.height = 1 + max( self.getNodeHeight(node.left), self.getNodeHeight(node.right) )
        root.height = 1 + max( self.getNodeHeight(root.left), self.getNodeHeight(root.right) )
        return root

    def rightRotate(self, node):
        root = node.left
        t = root.right
        node.left = t
        root.right = node
        node.height = 1 + max( self.getNodeHeight(node.left) - self.getNodeHeight(node.right) )
        root.height = 1 + max( self.getNodeHeight(root.left) - self.getNodeHeight(root.right) )
        return root

    def insert(self, node, data):
        if node is None:
            return self.buildNode(data)
        elif data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)
        # updating the heights of the nodes
        node.height = 1 + max( self.getNodeHeight(node.left), self.getNodeHeight(node.right) )

        # getting the balance factor to rotate the tree
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
            print("no need rotation")

        return node

    def delete(self, node, data):
        if not node:
            return node
        elif data < node.data:
            node.left = self.delete(node.left, data)
        elif data > node.data:
            node.right = self.delete(node.right, data)
        else:
            print("data found to be deleted")
            if node.left is None:
                t = node.right
                node = None
                return t
            elif node.right is None:
                t = node.left
                node = None
                return t
            temp = self.getSuccessor(node.right)
            node.data = temp.data
            node.right = self.delete(node.right, node.data)

        # updating the heights of the nodes
        node.height = 1 + max(self.getNodeHeight(node.left), self.getNodeHeight(node.right))

        # getting the balance factor to rotate the tree
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
            print("no need rotation")

        return node


