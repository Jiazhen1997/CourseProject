




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        
        self.ret = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.ret

    def dfs(self, node):
        
        if not node:
            return 0

        l = self.dfs(node.left)
        r = self.dfs(node.right)
        self.ret = max(self.ret, l + 1 + r - 1)  
        return max(l, r) + 1
