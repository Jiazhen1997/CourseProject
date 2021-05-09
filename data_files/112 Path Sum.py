
__author__ = 'Danyang'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        
        
        if not root:
            return False

        
        
        

        sum = sum-root.val

        
        if sum==0 and root.left is None and root.right is None:
            return True

        
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)




