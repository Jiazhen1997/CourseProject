
__author__ = 'Danyang'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        

        
        if not p and not q:
            return True

        
        try:
            if p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                return True
        except AttributeError:
            return False

        return False
