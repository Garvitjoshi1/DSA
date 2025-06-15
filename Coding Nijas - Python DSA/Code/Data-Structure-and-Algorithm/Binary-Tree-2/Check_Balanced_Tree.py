class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return None
    lh = height(root.left)
    rh = height(root.right)
    return max(lh, rh) + 1


#  this code is not providing us the most optimal time complexity as worst case is big(O*n^2) and best case is (O*n.logn)
# def isBalanced(root):
#     if root is None:
#         return True
#     lh = height(root.left)
#     rh = height(root.right)
#     if lh - rh > 1 and rh - lh > 1:
#         return False
#     isLeftBalanced = isBalanced(root.left)
#     isRightBalanced = isBalanced(root.right)
#     if isLeftBalanced and isRightBalanced:
#         return True
#     else:
#         return False

# the big(O(n)) approach is:-
def getHeightAndCheckBalanced(root):
    if root is None:
        return None
    lh, isLeftBalanced = getHeightAndCheckBalanced(root.left)
    rh, isRightBalanced = getHeightAndCheckBalanced(root.right)
    h = max(lh, rh)
    if lh - rh > 1 or rh - lh > 1:
        return h, False
    if isLeftBalanced and isRightBalanced:
        return h, True
    else:
        return h, False
