
__author__ = 'Danyang'



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        
        if not root:
            return True

        return self.isSymmetrical(root.left, root.right)

    def isSymmetrical(self, l, r):
        if not l and not r:
            return True

        
        if (l and r and
            l.val == r.val and self.isSymmetrical(l.left, r.right) and self.isSymmetrical(l.right, r.left)):
            return True

        return False
