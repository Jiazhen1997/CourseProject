




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.covered = {None}
        self.cnt = 0

    def minCameraCover(self, root: TreeNode) -> int:
        
        self.dfs(root, None)
        if root not in self.covered:
            self.covered.add(root)
            self.cnt += 1

        return self.cnt


    def dfs(self, node, pi):
        
        if not node:
            return

        self.dfs(node.left, node)
        self.dfs(node.right, node)
        if node.left not in self.covered or node.right not in self.covered:
            self.cnt += 1
            self.covered.add(node.left)
            self.covered.add(node.right)
            self.covered.add(node)
            self.covered.add(pi)


class SolutionErrror:
    def __init__(self):
        self.covered = set()

    def minCameraCover(self, root: TreeNode) -> int:
        
        dummy = TreeNode(0)
        dummy.left = root
        self.dfs(root, dummy)
        self.covered.discard(dummy)  
        return len(self.covered)

    def dfs(self, node, pi):
        
        if not node:
            return

        self.dfs(node.left, node)
        self.dfs(node.right, node)
        
        if (
            (not node.left or node.left in self.covered) and
            (not node.right or node.right in self.covered)
        ):
            self.covered.add(pi)
            return
