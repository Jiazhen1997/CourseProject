




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        
        return self.walk(root, L, R)

    def walk(self, node, L, R):
        if not node:
            return None

        node.left = self.walk(node.left, L, R)
        node.right = self.walk(node.right, L, R)
        if node.val < L:
            return node.right
        elif node.val > R:
            return node.left
        else:
            return node
