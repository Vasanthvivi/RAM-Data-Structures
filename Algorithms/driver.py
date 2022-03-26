from avlDriver import Tree
root = None
tree = Tree()
datas = [3,2,4,1,5]
for data in datas:
    root = tree.insert(root, data)
print(root)
