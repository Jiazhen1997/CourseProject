



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: 'TreeNode') -> int:
        
        ret = [float('inf')]  
        self.dfs(root, ret)
        return ret[0]

    def dfs(self, node, ret):
        if not node:
            return None, None
        left_min, left_max = self.dfs(node.left, ret)
        right_min, right_max = self.dfs(node.right, ret)
        if left_max:
            ret[0] = min(ret[0], abs(node.val - left_max))
        if right_min:
            ret[0] = min(ret[0], abs(node.val - right_min))
        left_min = left_min or node.val
        right_max = right_max or node.val
        return left_min, right_max
