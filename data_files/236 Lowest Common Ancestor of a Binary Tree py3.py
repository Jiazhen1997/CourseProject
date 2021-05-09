




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.count(root, p, q)
        return self.ans

    def count(self, node, p, q):
        if not node:
            return 0

        lcount = self.count(node.left, p, q)
        rcount = self.count(node.right, p, q)
        mcount = 1 if node == p or node == q else 0
        ret = lcount + rcount + mcount
        if lcount == 1 and rcount == 1 or lcount == 1 and mcount == 1 or rcount == 1 and mcount == 1:
            self.ans = node
        return ret
