




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.walk(root, p, q)

    def walk(self, node, p, q):
        if p.val > node.val and q.val > node.val:
            return self.walk(node.right, p, q)
        if p.val < node.val and q.val < node.val:
            return self.walk(node.left, p, q)
        return node
