
__author__ = 'Danyang'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        
        return self.fathom(root, 0)

    def fathom(self, root, depth):
        
        if not root: return depth
        elif root.right and not root.left: return self.fathom(root.right, depth+1)
        elif root.left and not root.right: return self.fathom(root.left, depth+1)
        else: return min(self.fathom(root.left, depth+1),
                         self.fathom(root.right, depth+1))