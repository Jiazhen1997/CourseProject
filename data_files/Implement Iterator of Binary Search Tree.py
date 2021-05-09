
__author__ = 'Danyang'


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def __init__(self, root):
        
        self.stk = []
        self.cur = root

    def hasNext(self):
        
        return self.cur or self.stk

    def next(self):
        
        if not self.hasNext():
            return None

        while self.cur:
            self.stk.append(self.cur)
            self.cur = self.cur.left

        node = self.stk.pop()  
        self.cur = node.right
        return node