
__author__ = 'Daniel'



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.s = 0

    def sumOfLeftLeaves(self, root):
        
        self.traverse(root)
        return self.s

    def traverse(self, node):
        if not node:
            return

        if node.left and not node.left.left and not node.left.right:
            self.s += node.left.val

        self.traverse(node.left)
        self.traverse(node.right)
