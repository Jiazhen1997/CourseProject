
__author__ = 'Danyang'


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def insertNode(self, root, node):
        
        cur = root
        if not root:
            root = node
            return root

        while cur:
            if cur.val == node.val:
                return root
            elif cur.val > node.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = node
                    return root
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = node
                    return root


