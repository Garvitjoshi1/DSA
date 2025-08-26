# define class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getLeafCount(node):
    if node is None:
        return 0
    if (node.left is None) and (node.right is None):
        return 1
    else:
        return getLeafCount(node.left) + getLeafCount(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Leaf count of tree is %d" % (getLeafCount(root)))
