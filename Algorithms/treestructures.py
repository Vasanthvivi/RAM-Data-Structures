class Node:
    def __init__(self, nodeData):
        self.left = None
        self.right = None
        self.data = nodeData


    # insertion
    def insertData(self,root, data):
        if not root:
            root = Node(data)
        elif data < root.data:
            if root.left:
                self.insertData(root.left, data)
            else:
                root.left = Node(data)
        elif data > root.data:
            if root.right:
                self.insertData(root.right, data)
            else:
                root.right = Node(data)
        else:
            print("not sure how this happened")

    #insertion via root
    def insertViaRoot(self, data):
        if not self:
            return Node(data)
        elif data < self.data:
            self.insertViaRoot( data)
        elif data > self.data:
            self.insertViaRoot( data)
        else:
            print("not sure how this happened")