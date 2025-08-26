class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()


def printTree(root):
    # this is an Edge case not base case.
    if root is None:
        return

    print(root.data)
    for child in root.children:
        printTree(child)


def printTreeDetailed(root):
    if root is None:
        return
    print(root.data, ":", end="")
    for child in root.children:
        print(child.data, ",", end="")
    print()
    for child in root.children:
        printTreeDetailed(child)


def takeTreeInput(rootData=int(input())):
    print("Enter root data")
    if rootData == -1:
        return None
    root = TreeNode(rootData)
    print("Enter number of children for ", rootData)
    childrenCount = int(input())
    for i in range(childrenCount):
        child = takeTreeInput()
        root.children.append(child)
    return root


import queue


def treeInputLevelWise(root):
    q = queue.Queue()
    print("Enter root")
    rootData = int(input())
    if rootData == -1:
        return None

    root = TreeNode(rootData)
    q.put(root)
    while (not(q.empty)):
        current_node = q.get()
        print("Enter num  of children for ", current_node.data)
        numChild = int(input())
        for i in range(numChild):
            print("Enter next child for ", current_node.data)
            childData = int(input())
            child = TreeNode(childData)
            current_node.children.append(child)
            q.put(child)
    return root


def numNode(root):
    count = 1
    for child in root.children:
        count = count + numNode(child)
        return count


root = takeTreeInput()
print(printTreeDetailed(root))
print("Number of Nodes In generic tree is: " + numNode(root))
