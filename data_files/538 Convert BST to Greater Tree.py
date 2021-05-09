



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: 'TreeNode') -> 'TreeNode':
        
        self.walk(root, 0)
        return root

    def walk(self, node, cur_sum):
        
        if not node:
            return cur_sum
        s = self.walk(node.right, cur_sum)
        node.val += s
        return self.walk(node.left, node.val)
