
__author__ = 'Daniel'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree_recur(self, root):
        
        if not root:
            return None

        self.invertTree_recur(root.left)
        self.invertTree_recur(root.right)
        root.left, root.right = root.right, root.left
        return root

    def invertTree(self, root):
        
        if not root:
            return None

        stk = []  
        post = []  

        stk.append(root)
        cur = None
        while stk:
            cur = stk.pop()
            post.append(cur)
            if cur.left:
                stk.append(cur.left)
            if cur.right:
                stk.append(cur.right)

        while post:
            cur = post.pop()
            cur.left, cur.right = cur.right, cur.left

        return cur