def NodeToRootPath(root, s):
    if root == None:
        return None
    if root.data == s:
        l = list()
        l.append(root.data)
        return
    leftOutput = NodeToRootPath(root.left, s)
    if leftOutput is not None:
        leftOutput.append(root.data)
        return leftOutput
    rightOutput = NodeToRootPath(root.right, s)
    if rightOutput is not None:
        rightOutput.append(root.data)
        return rightOutput
    else:
        return None
