# class defined
class Binary_Tree_Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def printTreeDetailed(root):
    if root is None:
        return
    print(root.data, end=':')
    if root.left is not None:
        print("L", root.left.data, end=',')
    if root.right is not None:
        print("R", root.right.data, end='')
    print()
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)


def treeInput():
    rootData = int(input())
    # base case
    if rootData == -1:
        return None
    root = Binary_Tree_Node(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root


root = treeInput()
print(printTreeDetailed(root))
