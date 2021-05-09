
__author__ = 'Daniel'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    def __init__(self, root):
        
        self.cur = root
        self.stk = []

    def hasNext(self):
        
        return self.cur or self.stk

    def next(self):
        
        while self.cur:
            self.stk.append(self.cur)
            self.cur = self.cur.left

        nxt = self.stk.pop()
        self.cur = nxt.right
        return nxt.val
