
__author__ = 'Daniel'


class Node(object):
    def __init__(self, lo, hi, cnt):
        self.lo = lo
        self.hi = hi
        self.cnt = cnt

        self.left = None
        self.right = None

    def __repr__(self):
        return repr("["%"d","%"d")"" ""%"" ""(""s""e""l""f"".""l""o"","" ""s""e""l""f"".""h""i"")"")""
""
""
""c""l""a""s""s"" ""S""e""g""m""e""n""t""T""r""e""e""(""o""b""j""e""c""t"")"":""
"" "" "" "" 
    def __init__(self):
        self.root = None

    def build(self, lo, hi):
        
        if lo >= hi: return
        if lo == hi-1: return Node(lo, hi, 1)

        root = Node(lo, hi, hi-lo)
        root.left = self.build(lo, (hi+lo)/2)
        root.right = self.build((lo+hi)/2, hi)
        return root

    def find_delete(self, root, val):
        
        root.cnt -= 1
        if not root.left:
            return root.lo
        elif root.left.cnt >= val:
            return self.find_delete(root.left, val)
        else:
            return self.find_delete(root.right,
                                    val - root.left.cnt)


class Solution(object):
    def reconstruct(self, A):
        st = SegmentTree()
        n = len(A)
        st.root = st.build(0, n)
        A = sorted(A, key=lambda x: x[0])
        ret = [0]*n
        for a in A:
            idx = st.find_delete(st.root, a[1]+1)
            ret[idx] = a[0]

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""A"" ""="" ""[""(""5"","" ""0"")"","" ""(""2"","" ""1"")"","" ""(""3"","" ""1"")"","" ""(""4"","" ""1"","")"","" ""(""1"","" ""4"")""]""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""r""e""c""o""n""s""t""r""u""c""t""(""A"")"" ""=""="" ""[""5"","" ""2"","" ""3"","" ""4"","" ""1""]