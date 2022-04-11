from avlhur import AVL
root = None
tree = AVL()
root = tree.insert(root, 3)
root = tree.insert(root, 1)
root = tree.insert(root, 5)
root = tree.insert(root, 6)
root = tree.insert(root, 7)
root = tree.delete(root, 7)
root = tree.delete(root, 6)
print(root)