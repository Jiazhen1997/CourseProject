
__author__ = 'Daniel'


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution(object):
    def searchRange(self, root, k1, k2):
        ret = []
        self.dfs(root, k1, k2, ret)
        return ret

    def dfs(self, root, k1, k2, ret):
        if not root:
            return

        if root.val < k1:
            self.dfs(root.right, k1, k2, ret)
        elif root.val > k2:
            self.dfs(root.left, k1, k2, ret)
        else:
            self.dfs(root.left, k1, k2, ret)
            ret.append(root.val)
            self.dfs(root.right, k1, k2, ret)