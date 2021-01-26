def max_path_sum(tree):
    _, maxSum = find_max_sum(tree)
    return maxSum


def find_max_sum(tree):
    if tree is None:
        return (0, 0)

    leftMaxSumAsBranch, leftMaxPathSum = find_max_sum(tree.left)
    rightMaxSumAsBranch, rightMaxPathSum = find_max_sum(tree.right)
    maxChildSumAsBranch = max(leftMaxSumAsBranch, rightMaxSumAsBranch)

    value = tree.value
    maxSumAsBranch = max(maxChildSumAsBranch + value, value)
    maxSumAsRootNode = max(
        leftMaxSumAsBranch + value + rightMaxSumAsBranch, maxSumAsBranch
    )
    max_path_sum = max(leftMaxPathSum, rightMaxPathSum, maxSumAsRootNode)

    return (maxSumAsBranch, max_path_sum)
