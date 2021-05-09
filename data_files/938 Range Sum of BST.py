




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ret = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        self.dfs(root, L, R)
        return self.ret

    def dfs(self, node, L, R):
        if not node:
            return

        if L <= node.val <= R:
            self.ret += node.val
            self.dfs(node.left, L, R)
            self.dfs(node.right, L, R)

        elif node.val > R:
            self.dfs(node.left, L, R)
        else:
            self.dfs(node.right, L, R)
