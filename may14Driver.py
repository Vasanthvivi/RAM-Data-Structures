from may14 import Tree
tree = Tree()
root = None
if __name__ == '__main__':
    for i in range(0, 5):
        root = tree.insertNode(root, i)
print(root)
# tree.inorder(root)
tree.descendingSorted(root)


