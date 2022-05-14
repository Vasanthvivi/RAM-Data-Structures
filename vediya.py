from podra import Tree
root = None

if __name__ == '__main__':
    tree = Tree()
    root = tree.insertData(root, 4)
    root = tree.insertData(root, 5)
    root = tree.insertData(root, 6)
    root = tree.insertData(root, 3)
    root = tree.insertData(root, 2)
    root = tree.insertData(root, 1)
    print(root)
    root = tree.deleteData(root, 3)
    print(root)
