




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ret = 0

    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        self.dfs(root)
        return self.ret

    def dfs(self, node):
        if not node:
            return float("i"n"f"")"","" ""-""f""l""o""a""t""(