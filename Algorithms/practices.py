class Node:
    counter = 1

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def towardsContext(self, root):
        if root:
            print(root.data)
            self.towardsContext(root.left)
            print("from context")
            print(root.data)
            print("------")
            self.towardsContext(root.right)

    def rotateLeft(self, node):
        if node:
            root = node.right
            node.right = root.left
            root.left = node


    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            if data > self.data:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def traverse(self, root):
        if root:
            self.traverse(root.left)
            print(root.data)
            self.traverse(root.right)

    def postOrderTraversal(self, root):
        if root:
            self.postOrderTraversal(root.left)
            self.postOrderTraversal(root.right)
            print(root.data)

    def printRight(self, root):
        if root:
            print(root.data)
            self.printRight(root.right)

    def printEndpoints(self, root):
        self.counter += 1
        print("counter",self.counter)
        if root:
            print(root.data)
            self.printEndpoints(root.left)
            # if self.counter == 3:
            #     self.printEndpoints(root.right)
            # else:
            #     print("skipped ", str(root.data))
