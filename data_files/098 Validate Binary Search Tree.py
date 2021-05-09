
__author__ = 'Danyang'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        
        if not root:
            return True

        if not self.isValidBST(root.left):
            return False
        if not self.isValidBST(root.right):
            return False

        if root.left:
            if not self.get_largest(root.left) < root.val:
                return False
        if root.right:
            if not root.val < self.get_smallest(root.right):
                return False


        return True

    def get_largest(self, root):
        
        if not root.right:
            return root.val
        return self.get_largest(root.right)

    def get_smallest(self, root):
        
        if not root.left:
            return root.val
        return self.get_smallest(root.left)



