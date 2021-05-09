




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        ret = self.find(root)
        return -1 if ret == float('inf') else ret

    def find(self, root: TreeNode) -> int:
        
        if not root:
            return float('inf')

        if root.left and root.right:
            if root.left.val == root.val:
                left = self.find(root.left)
            else:
                left = root.left.val

            if root.right.val == root.val:
                right = self.find(root.right)
            else:
                right = root.right.val

            return min(left, right)

        return float('inf')
