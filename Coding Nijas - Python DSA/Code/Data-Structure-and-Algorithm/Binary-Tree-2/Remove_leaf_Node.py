class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def remove(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return None
    root.left = remove(root.left)
    root.right = remove(root.right)
    return root

