




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.root = root
        return self.walk(root, k)

    def walk(self, node, k):
        if not node:
            return False

        target = k - node.val
        if self.find(self.root, target, node):
            return True

        if self.walk(node.left, k) or self.walk(node.right, k):
            return True

        return False

    def find(self, node, target, existing):
        if not node:
            return False

        if node.val == target:
            return node != existing

        if target < node.val:
            return self.find(node.left, target, existing)
        else:
            return self.find(node.right, target, existing)
