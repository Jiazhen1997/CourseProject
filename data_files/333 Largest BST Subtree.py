
import sys

__author__ = 'Daniel'



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTInfo(object):
    def __init__(self, sz, lo, hi):
        self.sz = sz
        self.lo = lo
        self.hi = hi


MAX = sys.maxint
MIN = -MAX - 1


class Solution(object):
    def __init__(self):
        self.gmax = 0

    def largestBSTSubtree(self, root):
        
        self.measure(root)
        return self.gmax

    def measure(self, root):
        if not root:
            return BSTInfo(0, MAX, MIN)

        left = self.measure(root.left)
        right = self.measure(root.right)
        if left.sz == -1 or right.sz == -1 or not left.hi <= root.val or not root.val <= right.lo:
            return BSTInfo(-1, MIN, MAX)

        sz = 1 + left.sz + right.sz
        self.gmax = max(self.gmax, sz)
        
        return BSTInfo(sz, min(root.val, left.lo), max(root.val, right.hi))


class SolutionError(object):
    def __init__(self):
        self.gmax = 0

    def largestBSTSubtree(self, root):
        
        self.measure(root)
        return self.gmax

    def measure(self, root):
        if not root:
            return 0

        left = self.measure(root.left)
        right = self.measure(root.right)

        if root.left and not root.val >= root.left.val or root.right and not root.val <= root.right.val:
            return 0

        if root.left and left == 0 or root.right and right == 0:
            return 0

        ret = 1 + left + right
        self.gmax = max(self.gmax, ret)
        return ret

if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""r""o""o""t"" ""="" ""T""r""e""e""N""o""d""e""(""1"")""
"" "" "" "" ""r""o""o""t"".""l""e""f""t"" ""="" ""T""r""e""e""N""o""d""e""(""2"")""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""l""a""r""g""e""s""t""B""S""T""S""u""b""t""r""e""e""(""r""o""o""t"")""
""
""
""
""
