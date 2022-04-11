class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data


class BinaryTree(object):

    # building a node
    def buildNode(self, data):
        return Node(data)

    # building branches
    def branch(self, node, data):
        if not node:
            return self.buildNode(data)
        elif data < node.data:
            node.left = self.branch(node.left, data)
        elif data > node.data:
            node.right = self.branch(node.right, data)
        return node

    def getSuccessor(self, node):
        if not node or node.left is None:
            return node
        return self.getSuccessor(node.left)

    # removing branches
    def removeBranch(self, node, data):
        if not node:
            return node
        elif data < node.data:
            node.left = self.removeBranch(node.left, data)
        elif data > node.data:
            node.right = self.removeBranch(node.right, data)
        else:
            # got the branch removing that
            print("we can delete node")
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
            node.right = self.removeBranch(node.right, node.data)
        return node