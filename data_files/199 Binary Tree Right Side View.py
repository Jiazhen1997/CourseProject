
__author__ = 'Daniel'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root):
        
        cur_lvl = []
        nxt_lvl = []
        ret = []

        if root:
            cur_lvl.append(root)

        while cur_lvl:
            ret.append(cur_lvl[-1].val)
            while cur_lvl:
                cur = cur_lvl.pop(0)
                if cur.left: nxt_lvl.append(cur.left)
                if cur.right: nxt_lvl.append(cur.right)

            cur_lvl = nxt_lvl
            nxt_lvl = []

        return ret