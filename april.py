class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        self.height = 1


class Tree(object):
    # building a node
    def buildNode(self, data):
        return Node(data)


    # building strands
    def insertNode(self, node, data):
        if node is None:
            return self.buildNode(data)
        elif data < node.data:
            node.left = self.insertNode(node.left, data)
        else:
            node.right = self.insertNode(node.right, data)
        print(f"now in {data}")
        return node