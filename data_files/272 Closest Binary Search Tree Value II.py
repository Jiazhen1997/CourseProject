
__author__ = 'Daniel'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestKValues(self, root, target, k):
        
        pre = []
        suc = []
        self.predecessors(root, target, pre)
        self.successors(root, target, suc)
        return self.merge(target, k, pre, suc)

    def predecessors(self, root, target, stk):
        if not root:
            return

        self.predecessors(root.left, target, stk)
        if root.val <= target:
            stk.append(root.val)
            self.predecessors(root.right, target, stk)

    def successors(self, root, target, stk):
        if not root:
            return

        self.successors(root.right, target, stk)
        if root.val > target:
            stk.append(root.val)
            self.successors(root.left, target, stk)

    def merge(self, target, k, pre, suc):
        ret = []
        while len(ret) < k:
            if not pre:
                ret.append(suc.pop())
            elif not suc:
                ret.append(pre.pop())
            elif abs(pre[-1] - target) < abs(suc[-1] - target):
                ret.append(pre.pop())
            else:
                ret.append(suc.pop())
        return ret