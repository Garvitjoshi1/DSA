# class defined
class Binary_Tree_Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


# Trees are mostly solved using recursion.
# function made
def printTree(root):
    # base case
    if root is None:
        return
    print(root.data)
    # recursion called -->
    printTree(root.left)
    printTree(root.right)


# function to print nodes and root along with the relations.
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


bt1 = Binary_Tree_Node(1)
btn2 = Binary_Tree_Node(2)
btn3 = Binary_Tree_Node(3)
btn4 = Binary_Tree_Node(4)
btn5 = Binary_Tree_Node(5)
bt1.left = btn2
bt1.right = btn3
btn2.left = btn4
btn2.right = btn5

print(printTree(bt1))

print(printTreeDetailed(bt1))


def treeInput():
    rootData = input()
    root = Binary_Tree_Node(rootData)
    leftTree = treeInput()
    rightTree = treeInput()
    root.left = leftTree
    root.right = rightTree
    return root
