
from collections import defaultdict

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

    def find_delete(self, root, sz):
        
        root.cnt -= 1
        if not root.left:
            return root.lo
        elif root.left.cnt >= sz:
            return self.find_delete(root.left, sz)
        else:
            return self.find_delete(root.right,
                                    sz-root.left.cnt)


class Solution(object):
    def reconstructQueue(self, A):
        

        def cmp(a, b):
            if a[0] != b[0]:
                return a[0]-b[0]
            else:
                return a[1]-b[1]

        st = SegmentTree()
        n = len(A)
        st.root = st.build(0, n)
        A.sort(cmp=cmp)
        ret = [0]*n
        ret_cnt = defaultdict(int)  
        for a in A:
            val, inv = a
            idx = st.find_delete(st.root, inv+1-ret_cnt[val])
            ret_cnt[val] += 1
            ret[idx] = a

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""r""e""c""o""n""s""t""r""u""c""t""Q""u""e""u""e""(""
"" "" "" "" "" "" "" "" ""[""[""9"","" ""0""]"","" ""[""7"","" ""0""]"","" ""[""1"","" ""9""]"","" ""[""3"","" ""0""]"","" ""[""2"","" ""7""]"","" ""[""5"","" ""3""]"","" ""[""6"","" ""0""]"","" ""[""3"","" ""4""]"","" ""[""6"","" ""2""]"","" ""[""5"","" ""2""]""]"")"" ""=""="" ""[""[""3"","" ""0""]"","" ""[""6"","" ""0""]"","" ""[""7"","" ""0""]"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""[""5"","" ""2""]"","" ""[""3"","" ""4""]"","" ""[""5"","" ""3""]"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""[""6"","" ""2""]"","" ""[""2"","" ""7""]"","" ""[""9"","" ""0""]"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""[""1"","" ""9""]""]