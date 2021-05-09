



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.dfs(root, root.val if root else None)

    def dfs(self, node, val) -> bool:
        if not node:
            return True
        if node.val != val:
            return False

        return self.dfs(node.left, val) and self.dfs(node.right, val)
