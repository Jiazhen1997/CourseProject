
__author__ = 'Daniel'


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution(object):
    def generateTrees(self, n):
        
        return self.dfs(1, n+1)

    def dfs(self, s, e):
        ret = []
        if s >= e:
            return [None]

        for i in xrange(s, e):
            ls = self.dfs(s, i)
            rs = self.dfs(i+1, e)
            for l in ls:
                for r in rs:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    ret.append(root)

        return ret