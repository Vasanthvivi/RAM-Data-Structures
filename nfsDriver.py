from avl import AVLTree
from nfs import MyTree
root = None
tree = MyTree()
root = tree.insert(root, 3)
# root = tree.insert_node(root, 1)
# root = tree.insert_node(root, 5)
# root = tree.insert_node(root, 4)
# root = tree.insert_node(root, 2)
root = tree.insert(root, 5)
root = tree.deleteNode(root, 5)
print(root)
