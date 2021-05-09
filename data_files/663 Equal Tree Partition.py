



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.sums = []

    def checkEqualTree(self, root: TreeNode) -> bool:
        
        self.dfs(root)
        total = self.sums.pop()
        return total % 2 == 0 and total // 2 in self.sums

    def dfs(self, node):
        if not node:
            return 0

        l = self.dfs(node.left)
        r = self.dfs(node.right)
        s = l + r + node.val
        self.sums.append(s)
        return s


class Solution:
    def __init__(self):
        
        self.exists = False
        self.root = None  
        self.total_sum = None

    def checkEqualTree(self, root: TreeNode) -> bool:
        
        self.root = root
        self.total_sum = self.dfs(root)
        self.dfs(root)
        return self.exists

    def dfs(self, node):
        if not node:
            return 0

        l = self.dfs(node.left)
        r = self.dfs(node.right)
        s = l + r + node.val
        if node != self.root and self.total_sum != None and self.total_sum == s * 2:
            self.exists = True

        return s
