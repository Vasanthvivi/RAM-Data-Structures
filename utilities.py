class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data


class binaryTree:
    # building strands of the tree
    def buildStrands(self, data):
        return Node(data)

    # building the strands of the tree
    def insertion(self, node, data):
        if not node:
            return self.buildStrands(data)
        elif data < node.data:
            node.left = self.insertion(node.left, data)
        else:
            node.right = self.insertion(node.right, data)
        return node

    def leftSide(self, node):
        if not node:
            print("base case")
        else:
            print(node.data)
            self.leftSide(node.left)
            print(node.data)

    def rightSide(self, node):
        if not node:
            pass
        else:
            self.rightSide(node.right)
            print(node.data)

    def leftBottom(self, node):
        if not node.left:
            print(node.data)
        else:
            self.leftBottom(node.left)


    def rightBottom(self, node):
        if not node.right:
            print(node.data)
        else:
            self.rightBottom(node.right)


    def treeLeaves(self, root):
        if root is None:
            print("base case")
        else:
            print(root.data)
            self.treeLeaves(root.left)
