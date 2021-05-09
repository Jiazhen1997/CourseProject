

__author__ = 'Daniel'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root, k):
        
        l = self.cnt(root.left)
        if l+1 == k:
            return root.val
        elif l+1 < k:
            return self.kthSmallest(root.right, k-(l+1))
        else:
            return self.kthSmallest(root.left, k)

    def cnt(self, root):
        if not root:
            return 0

        return 1+self.cnt(root.left)+self.cnt(root.right)