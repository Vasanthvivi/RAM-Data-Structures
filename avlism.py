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
        # Update the balance factor and balance the tree
        balanceFactor = self.getBalance(node)
        if balanceFactor > 1:
            if data < node.left.data:
                return self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)

        if balanceFactor < -1:
            if data > node.right.data:
                return self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)
        return node

    # Function to delete a node
    def delete_node(self, root, key):
        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.data:
            root.left = self.delete_node(root.left, key)
        elif key > root.data:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right,
                                          temp.data)
        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    # get node height
    def getHeight(self, node):
        if not node:
            return 0
        else:
            return node.height

    # rotate tree in left side
    def leftRotate(self, node):
        root = node.right
        rotatorRightNode = root.left
        root.left = node
        node.right = rotatorRightNode
        node.height = 1 + max(self.getHeight(node.left),
                           self.getHeight(node.right))
        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
        return root

    # rotate tree in right side
    def rightRotate(self, node):
        root = node.left
        rotatorLeftNode = root.right
        root.right = node
        node.left = rotatorLeftNode
        node.height = 1 + max(self.getHeight(node.left),
                              self.getHeight(node.right))
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))
        return root

    # Get balance factore of the node
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

