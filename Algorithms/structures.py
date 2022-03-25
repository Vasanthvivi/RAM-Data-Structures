class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
            print("inserted")
        elif data < self.data:
            if self.left is None:
                self.left = Node(data)
                print("inserted")
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
                print("inserted")
            else:
                self.right.insert(data)
        else:
            print("Not sure how this happened")

    def insertViaRoot(self, root, data):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = root.insertViaRoot(root.left, data)
        elif data > root.data:
            root.right = root.insertViaRoot(root.right, data)
        else:
            print("not sure how this happened")


    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def preorder(self, root):
        if root is None:
            print("depth reached")
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data)
        else:
            print("depth reached")
