



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.pi = []
        self.depths = []

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        self.dfs(None, root, x, 0)
        self.dfs(None, root, y, 0)
        if len(self.pi) != 2:
            return False
        return self.pi[0] != self.pi[1] and self.depths[0] == self.depths[1]


    def dfs(self, pi, node, x, depth):
        if not node:
            return

        if node.val == x:
            self.pi.append(pi)
            self.depths.append(depth)
            return

        self.dfs(node, node.left, x, depth + 1)
        self.dfs(node, node.right, x, depth + 1)
