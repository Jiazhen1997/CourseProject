
__author__ = 'Danyang'


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution(object):
    def maxTree(self, A):
        
        stk = []
        for a in A:
            cur = TreeNode(a)
            while stk and stk[-1].val <= cur.val:
                pre = stk.pop()
                pre.right = cur.left
                cur.left = pre

            stk.append(cur)

        pre = None
        while stk:
            cur = stk.pop()
            cur.right = pre
            pre = cur

        return pre
