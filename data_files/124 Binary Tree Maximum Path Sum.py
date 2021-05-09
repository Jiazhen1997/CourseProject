
__author__ = 'Danyang'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    global_max = -1<<31
    def maxPathSum(self, root):
        
        self.get_max_component(root)
        
        return self.global_max

    def get_max_component(self, root):
        
        if not root:
            return 0

        left_max_component = self.get_max_component(root.left)
        right_max_component = self.get_max_component(root.right)

        
        current_max_sum = max(root.val, root.val+left_max_component, root.val+right_max_component, root.val+left_max_component+right_max_component)  
        self.global_max = max(self.global_max, current_max_sum)

        
        return max(root.val, root.val+left_max_component, root.val+right_max_component)  




