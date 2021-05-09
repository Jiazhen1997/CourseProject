
__author__ = 'Daniel'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.val)


class Solution:
    def countNodes(self, root):
        
        if not root:
            return 0
        h = self.get_height(root)
        h_r = self.get_height(root.right)
        if h == h_r+1:
            return 2**(h-1)-1+1+self.countNodes(root.right)  
        else:
            return 2**(h-2)-1+1+self.countNodes(root.left)  

    def get_height(self, cur):
        h = 0  
        while cur:
            h += 1
            cur = cur.left

        return h


class Solution_TLE:
    def __init__(self):
        self.depth = 0  
        self.cnt = 0
        self.stopped = False

    def countNodes(self, root):
        
        if not root:
            return 0
        self.get_depth(root)
        self.fanthom(root, 1)
        return 2**(self.depth-1)-1+self.cnt

    def get_depth(self, root):
        self.depth += 1
        if root.left:
            self.get_depth(root.left)

    def fanthom(self, root, depth):
        if self.stopped:
            return

        if not root.left and not root.left:
            if self.depth == depth:
                self.cnt += 1
            else:
                self.stopped = True
            return

        if root.left:
            self.fanthom(root.left, depth+1)
        if root.right:
            self.fanthom(root.right, depth+1)

    def countNodes_TLE(self, root):
        
        if not root:
            return 0

        return 1+self.countNodes(root.left)+self.countNodes(root.right)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""a""s""s""
