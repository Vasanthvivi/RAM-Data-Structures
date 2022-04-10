class Node:
    def __init__(self, _data):
        self.left = None
        self.right = None
        self.data = _data
        self.height = 1

    def getHeight(self, root):
        if root:
            return root.height
        else:
            return 0

    def insertFunction(self,data):
        if self:
            if data < self.data:
               if self.left:
                   self.left.insertFunction(data)
                   self.left.height += 1
                   print(self.left.height)
               else:
                   self.left = Node(data)
            elif data > self.data:
                if self.right:
                    self.right.insertFunction(data)
                    self.right.height += 1
                    print(self.right.height)
                else:
                    self.right = Node(data)
            else:
                print("not sure how this happended")
