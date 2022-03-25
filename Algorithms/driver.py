from avlDriver import Tree
root = None
tree = Tree()
datas = [1,2,3,4,5]
for data in datas:
    root = tree.insert(root, data)
print(root)
root = tree.insert(root, 4)
root = tree.insert(root, 5)
root = tree.insert(root, 3)