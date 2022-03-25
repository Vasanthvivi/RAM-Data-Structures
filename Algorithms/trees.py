from practices import Node
from avl import AVLTree
# from structures import Node
from treestructures import Node
# root = None
# root = Node(3)
# root.insertData(root, 1)
# root.insertData(root, 4)
# root.insertData(root, 5)
# print(root)
# root = Node(3)
# leftChild = Node(1)
# rightChild = Node(5)
# root.left = leftChild
# root.right = rightChild
# print(root)

# using the insertData method

myTree = AVLTree()
root = Node(3)
# root = None
nums = [1, 4, 5, 6]
for num in nums:
    # root = root.insertViaRoot( num)
    root.insert_node(root, num)

print(root)
# myTree.printHelper(root, "", True)
# key = 13
# root = myTree.delete_node(root, key)
# print("After Deletion: ")
# myTree.printHelper(root, "", True)


# root = None
# root = AVLTree(3)
# root.insert(1)
# # root.insert(2)
# # root.insert(0)
# root.insert(4)
# root.insert(5)
# root.insert(7)
# root.rotateLeft()
# root.insert(6)
# root.insert(10)
# root.towardsContext(root)

# root.printEndpoints(root)
# root.inorder(root)
# root.preorder(root)
# root.postorder(root)