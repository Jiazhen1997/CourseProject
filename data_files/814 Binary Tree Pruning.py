




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import Tuple


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        root, _ = self.prune(root)
        return root

    def prune(self, node) -> Tuple[TreeNode, bool]:
        if not node:
            return None, False

        node.left, contain_left = self.prune(node.left)
        node.right, contain_right = self.prune(node.right)
        if not contain_left and not contain_right and node.val == 0:
            return None, False

        return node, True
