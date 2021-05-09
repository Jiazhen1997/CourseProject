




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return

        node = TreeNode(0)
        node.val += t1 and t1.val or 0
        node.val += t2 and t2.val or 0
        node.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        node.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
        return node
