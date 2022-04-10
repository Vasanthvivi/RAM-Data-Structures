class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self is None:
            self = Node(data)
        elif data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        elif data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
        else:
            print(data)
