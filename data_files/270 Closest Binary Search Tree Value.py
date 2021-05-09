
import sys

__author__ = 'Daniel'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def closestValue(self, root, target):
        
        lo = [-sys.float_info.max]
        self.find(root, target, lo, True)
        hi = [sys.float_info.max]
        self.find(root, target, hi, False)
        if hi[0] - target < target - lo[0]:
            return int(hi[0])
        else:
            return int(lo[0])

    def find(self, root, target, ret, lower=True):
        if not root:
            return

        if root.val == target:
            ret[0] = root.val
            return

        if root.val < target:
            if lower: ret[0] = max(ret[0], root.val)
            self.find(root.right, target, ret, lower)
        else:
            if not lower: ret[0] = min(ret[0], root.val)
            self.find(root.left, target, ret, lower)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""l""o""s""e""s""t""V""a""l""u""e""(""T""r""e""e""N""o""d""e""(""2""1""4""7""4""8""3""6""4""7"")"","" ""0"".""0"")"" ""=""="" ""2""1""4""7""4""8""3""6""4""7""
