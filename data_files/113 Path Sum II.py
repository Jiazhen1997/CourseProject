
__author__ = 'Danyang'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        
        result = []
        self.accumulatePathSum(root, sum, [], result)
        return result

    def accumulatePathSum(self, root, sum, cur_path, result):
        
        
        if not root:
            return

        sum = sum - root.val
        cur_path.append(root.val)
        
        if sum==0 and root.left is None and root.right is None:
            result.append(list(cur_path))  
            return

        
        if root.left: self.accumulatePathSum(root.left, sum, list(cur_path), result)  
        if root.right: self.accumulatePathSum(root.right, sum, list(cur_path), result)  
