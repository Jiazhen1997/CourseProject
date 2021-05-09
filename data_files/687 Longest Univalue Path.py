



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ret = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.find(root)
        return self.ret

    def find(self, node):
        
        if not node:
            return 0

        left = self.find(node.left)
        right = self.find(node.right)
        left_path = left + 1 if node.left and node.left.val == node.val else 0
        right_path = right + 1 if node.right and node.right.val == node.val else 0
        self.ret = max(self.ret, left_path + right_path)
        return max(left_path, right_path)


class Solution_error:
    def __init__(self):
        self.ret = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.find(root)
        return self.ret

    def find(self, node):
        
        if not node:
            return 0

        left = self.find(node.left)
        right = self.find(node.right)
        cur = 1  
        path = 1
        if left and node.left.val == node.val:
            path += left
            cur = left + 1

        if right and node.right.val == node.val:
            path += right
            if right > left:
                cur = right + 1

        self.ret = max(self.ret, path - 1)
        return cur
