




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.prev = None
        self.root = None

    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        self.dfs(root)
        return self.root

    def dfs(self, node):
        if not node:
            return

        self.dfs(node.left)
        if not self.prev:
            self.root = node
        else:
            self.prev.right = node
            node.left = None  

        self.prev = node
        self.dfs(node.right)
