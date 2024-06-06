class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isValidSequence(root: TreeNode, arr: [int]) -> bool:
    def dfs(node, index):
        if not node:
            return False
        if index >= len(arr) or node.val != arr[index]:
            return False
        if index == len(arr) - 1:
            return not node.left and not node.right

        return dfs(node.left, index + 1) or dfs(node.right, index + 1)

    return dfs(root, 0)


# Example usage:
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = TreeNode(0)
root.left.left.right = TreeNode(1)
root.left.right.left = TreeNode(0)
root.left.right.right = TreeNode(0)

arr1 = [0, 1, 0, 1]
print(isValidSequence(root, arr1))  # Output: True

arr2 = [0, 0, 1]
print(isValidSequence(root, arr2))  # Output: False

arr3 = [0, 1, 1]
print(isValidSequence(root, arr3))  # Output: False
