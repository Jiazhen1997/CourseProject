
__author__ = 'Danyang'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    
    
    def maxDepth(self, root):
        
        return self.fathom(root, 0)

    def fathom(self, root, depth):
        
        if not root: return depth
        else: return max(self.fathom(root.left, depth+1), self.fathom(root.right, depth+1))
