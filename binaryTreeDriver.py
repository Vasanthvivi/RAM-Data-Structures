from binaryTree import BinaryTree
root = None
tree = BinaryTree()
root = tree.branch(root, 3)
root = tree.branch(root, 1)
root = tree.branch(root, 6)
root = tree.branch(root, 5)
root = tree.branch(root, 4)
root = tree.removeBranch(root, 3)
print(root)