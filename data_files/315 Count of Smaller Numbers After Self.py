
__author__ = 'Daniel'


class TreeNode(object):
    def __init__(self, start, end, cnt=0):
        self.start = start
        self.end = end
        self.cnt = cnt
        self.left = None
        self.right = None


class SegmentTree(object):
    def __init__(self, n):
        self.root = self.build(0, n)

    def build(self, start, end):
        if start >= end: return
        if start == end-1: return TreeNode(start, end)
        node = TreeNode(start, end)
        node.left = self.build(start, (start+end)/2)
        node.right = self.build((start+end)/2, end)
        return node

    def inc(self, idx, val):
        cur = self.root
        while cur:
            cur.cnt += val
            mid = (cur.start+cur.end)/2
            if cur.start <= idx < mid:
                cur = cur.left
            elif mid <= idx < cur.end:
                cur = cur.right
            else:
                return

    def query_less(self, cur, idx):
        if not cur:
            return 0

        mid = (cur.start+cur.end)/2
        if cur.start <= idx < mid:
            return self.query_less(cur.left, idx)
        elif mid <= idx < cur.end:
            return (cur.left.cnt if cur.left else 0) + self.query_less(cur.right, idx)
        else:
            return 0


class Solution(object):
    def countSmaller(self, nums):
        
        
        h = {}
        for i, v in enumerate(sorted(nums)):
            h[v] = i  

        A = [h[v] for v in nums]
        n = len(A)
        st = SegmentTree(n)
        ret = []
        for i in xrange(n-1, -1, -1):
            ret.append(st.query_less(st.root, A[i]))
            st.inc(A[i], 1)

        return ret[::-1]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""o""u""n""t""S""m""a""l""l""e""r""(""[""5"","" ""2"","" ""6"","" ""1""]"")"" ""=""="" ""[""2"","" ""1"","" ""1"","" ""0""]""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""o""u""n""t""S""m""a""l""l""e""r""(""[""-""1"","" ""-""1""]"")"" ""=""="" ""[""0"","" ""0""]""
