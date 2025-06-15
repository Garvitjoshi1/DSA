from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


import queue


def nextLargest(tree, n):
    if tree is None:
        return
    if tree.data > n:
        ans = tree
    else:
        ans = None

    q = queue.Queue()
    q.put(tree)

    while not (q.empty()):
        current_node = q.get()

        for child in current_node.children:
            if n < child.data < ans:
                ans = child.data
    return child


def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root


# Main
n = int(input())
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(nextLargest(tree, n).data)
