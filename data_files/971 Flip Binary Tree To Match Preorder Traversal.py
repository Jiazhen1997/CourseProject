

from typing import List



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ret = []
        self.i = 0  

    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        
        self.dfs(root, voyage)
        return self.ret

    def dfs(self, node, voyage):
        if not node:
            return

        if node.val != voyage[self.i]:
            self.ret = [-1]
            return

        self.i += 1
        if node.left and node.right and node.left.val != voyage[self.i]:
            
            self.ret.append(node.val)
            self.dfs(node.right, voyage)
            self.dfs(node.left, voyage)
        else:
            self.dfs(node.left, voyage)
            self.dfs(node.right, voyage)
