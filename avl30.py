# root structure
class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None
        self.height = 1


# building the tree
class Tree:
    #     build node either root or child
    def buildNode(self, data):
        return Node(data)

    # inserting trees
    def insert(self, node, data):
        if not node:
            return self.buildNode(data)
        elif data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        bf = self.getBalanceFactor(node)
        if bf < -1:
            print("do left rotation")
            if data > node.right.data:
                return self.leftRotateNode(node)
            else:
                node.right = self.rightRotateNode(node.right)
                return self.leftRotateNode(node)
        elif bf > 1:
            print("do right rotation")
            if data < node.left.data:
                return self.rightRotateNode(node)
            else:
                node.left = self.leftRotateNode(node.left)
                return self.leftRotateNode(node)
        elif bf == 0:
            print("node ",node.data," is perfectly balanced")
        return node

    # getting the height of the node
    def getHeight(self, node):
        if not node:
            return 0
        else:
            return node.height

    def getBalanceFactor(self, node):
        if not node:
            return 0
        else:
            return self.getHeight(node.left) - self.getHeight(node.right)


    def leftRotateNode(self, node):
        root = node.right
        node.right = root.left
        root.left = node
        root.height = max(self.getHeight(root.left), self.getHeight(root.right)) + 1
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        return root

    def rightRotateNode(self, node):
        root = node.left
        node.left = root.right
        root.right = node
        root.height = max(self.getHeight(root.left), self.getHeight(root.right)) + 1
        node.height = max(self.getHeight(node.left), self.getHeight(node.right)) + 1
        return root
