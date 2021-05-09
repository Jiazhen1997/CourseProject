




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.prev = None
        self.ret = float('inf')

    def minDiffInBST(self, root: TreeNode) -> int:
        
        if not root:
            return

        self.minDiffInBST(root.left)
        if self.prev:
            self.ret = min(self.ret, root.val - self.prev)
        self.prev = root.val
        self.minDiffInBST(root.right)
        return self.ret
