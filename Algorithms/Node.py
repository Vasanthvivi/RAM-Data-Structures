class Node:
    def __init__(self):
        self.left = Node
        self.right = Node
        self.data = 0

    def insertdata(self, currentData):
        if self.data == 0:
            self.data = currentData
        elif currentData < self.data:
            if self.left().data == 0:
                self.left.insertdata(currentData)
            else:
                print("left child insertData() failed")
        elif currentData > self.data:
            if self.right().data == 0:
                self.right.insertdata(currentData)
            else:
                print("right child insertData() failed")
        else:
            print("not sure how this happened")



