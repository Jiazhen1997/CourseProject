




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ret = 0
        self.lst = []

    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        self.dfs(root)
        return self.ret

    def dfs(self, node):
        if not node:
            return

        self.lst.append(node.val)  
        if not node.left and not node.right:
            
            cur = 0
            for a in self.lst:
                cur <<= 1
                cur += a
            self.ret += cur
        else:
            self.dfs(node.left)
            self.dfs(node.right)
        self.lst.pop()
