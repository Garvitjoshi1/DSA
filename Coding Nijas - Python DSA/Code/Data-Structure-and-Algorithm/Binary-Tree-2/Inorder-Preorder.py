class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def buildTree(pre, inorder):
    if len(pre) == 0:
        return None
    rootData = pre[0]
    root = BinaryTreeNode(rootData)
    rootIndexInorder = -1
    for i in range(0, len(inorder)):
        if inorder[i] == rootData:
            break
    if rootIndexInorder == -1:
        return None

    leftInorder = inorder[0: rootIndexInorder]
    rightInorder = inorder[rootIndexInorder + 1:]

    lenLeftSubTree = len(leftInorder)

    leftPreOder = pre[1:lenLeftSubTree + 1]
    rightPreOrder = pre[lenLeftSubTree + 1:]

    leftChild = buildTree(leftPreOder, leftInorder)
    rightChild = buildTree(rightPreOrder, rightInorder)

    root.left = leftChild
    root.right = rightChild
    return root


pre = [1, 2, 4, 5, 3, 6, 7]
inorder = [4, 2, 5, 1, 6, 3, 7]
print(buildTree(pre, inorder))
