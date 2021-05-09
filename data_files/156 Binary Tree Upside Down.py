
__author__ = 'Daniel'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def upsideDownBinaryTree(self, root):
        
        if not root or not root.left:
            return root

        left, right = root.left, root.right
        root_new = self.upsideDownBinaryTree(root.left)
        left.left, left.right = right, root
        root.left, root.right = None, None
        return root_new


class SolutionComplex(object):
    def __init__(self):
        self.root = TreeNode(0)
        self.cur_new = self.root

    def upsideDownBinaryTree(self, root):
        
        if not root:
            return

        self.traverse(root)
        return self.root

    def traverse(self, cur):
        
        if not cur:
            return

        if not cur.left:
            self.cur_new.val = cur.val
            return

        self.traverse(cur.left)
        if cur.right: self.cur_new.left = TreeNode(cur.right.val)
        self.cur_new.right = TreeNode(cur.val)
        self.cur_new = self.cur_new.right