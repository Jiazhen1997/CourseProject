
__author__ = 'Daniel'



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findLeaves(self, root):
        
        leaves = []
        self.dfs(root, leaves)
        return leaves

    def dfs(self, node, leaves):
        
        if not node:
            return -1  

        height = 1 + max(self.dfs(node.left, leaves), self.dfs(node.right, leaves))
        if height >= len(leaves):
            leaves.append([])  

        leaves[height].append(node.val)
        return height
