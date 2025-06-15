from Data_Structure_and_Algorithm.Binary_Tree_1.Main import printTreeDetailed, treeInput


def printDepthK(root, k):
    if root is None:
        return
    if k == 0:
        print(root.data)
        return
    printDepthK(root.left, k - 1)
    printDepthK(root.right, k + 1)


def printDepthKV2(root, k, d=0):
    if root is None:
        return
    if k == d:
        print(root.data)
        return
    printDepthKV2(root.left, k, d+1)
    printDepthKV2(root.right, k, d+1)


root = treeInput()
print(printTreeDetailed(root))
print(printDepthK(root, 2))