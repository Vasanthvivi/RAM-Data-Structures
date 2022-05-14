from apr30 import TreeDriver
root = None

if __name__ == "__main__":
    # data = [1,2,3,4,5,6,]
    tree = TreeDriver()
    # for d in data:
    #     root = tree.buildNode(root, d)
    # print(root)
    for d in range(0, 100000):
        root = tree.buildNode(root, d)
    tree.find(root, 9898)

