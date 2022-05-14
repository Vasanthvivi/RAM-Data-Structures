from may import DriverTree
root = None

if __name__ == "__main__":
    # data = [1,2,3,4,5,6,]
    tree = DriverTree()
    # for d in data:
    #     root = tree.buildNode(root, d)
    # print(root)
    for d in range(1, 1001):
        root = tree.buildStrand(root, d)
    root = tree.deleteNode(root, 4)
    print(root)