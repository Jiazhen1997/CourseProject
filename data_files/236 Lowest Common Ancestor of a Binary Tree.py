

__author__ = 'Daniel'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        
        path1, path2 = [], []
        self.dfs(root, p, path1, [False])
        self.dfs(root, q, path2, [False])

        i = 0
        while i < min(len(path1), len(path2)):
            if path1[i] != path2[i]:
                return path1[i-1]
            i += 1

        return path1[i-1]

    def dfs(self, root, t, path, found):
        if not root or found[0]:  
            return

        path.append(root)
        if root == t:
            found[0] = True

        self.dfs(root.left, t, path, found)
        self.dfs(root.right, t, path, found)
        if not found[0]:
            path.pop()  

