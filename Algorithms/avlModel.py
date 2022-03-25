class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(Node):

    # inserting nodes
    def insertPerfectly(self, data):
        if not self:
            self = Node(data)
        else:
            if data > self.data:
                if self.right:
                    self.right.insertPerfectly(data)
                else:
                    self.right = Node(data)
            elif data < self.data:
                if self.left:
                    self.left.insertPerfectly(data)
                else:
                    self.left = Node(data)