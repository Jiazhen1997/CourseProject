




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        ret = [0]
        self.walk(root, ret)
        return ret[0]

    def walk(self, node: TreeNode, ret) -> int:
        
        if not node:
            return 0

        l = self.walk(node.left, ret)
        r = self.walk(node.right, ret)
        ret[0] += abs(l - r)
        return l + node.val + r
