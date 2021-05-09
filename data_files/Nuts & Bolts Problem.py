
__author__ = 'Daniel'
try:
    from lintcode import Compare
except ImportError:
    class Compare:
        @classmethod
        def cmp(cls, a, b):
            
            a = a.lower()
            b = b.lower()

            diff = ord(a)-ord(b)
            if diff < 0:
                return -1
            elif diff > 0:
                return 1
            else:
                return 0


class Solution:
    def sortNutsAndBolts(self, nuts, bolts):
        
        assert len(nuts) == len(bolts)
        self.quick_sort(nuts, bolts, 0, len(nuts))

    def quick_sort(self, nuts, bolts, start, end):
        
        if start >= end:
            return

        pivot = self.partition(nuts, bolts[start], start, end)
        self.partition(bolts, nuts[pivot], start, end)
        self.quick_sort(nuts, bolts, start, pivot)
        self.quick_sort(nuts, bolts, pivot+1, end)

    def partition(self, A, pivot, start, end):
        
        left = start  
        i = start+1
        while i < end:
            if Compare.cmp(A[i], pivot) == -1 or Compare.cmp(pivot, A[i]) == 1:
                left += 1
                A[left], A[i] = A[i], A[left]
                i += 1
            elif Compare.cmp(A[i], pivot) == 0 or Compare.cmp(pivot, A[i]) == 0:
                A[start], A[i] = A[i], A[start]
            else:
                i += 1

        
        A[start], A[left] = A[left], A[start]

        return left


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""n""u""t""s"" ""="" ""[""'""a""'"","" ""'""b""'"","" ""'""d""'"","" ""'""g""'""]""
"" "" "" "" ""b""o""l""t""s"" ""="" ""[""'""A""'"","" ""'""G""'"","" ""'""D""'"","" ""'""B""'""]""
"" "" "" "" ""S""o""l""u""t""i""o""n""("")"".""s""o""r""t""N""u""t""s""A""n""d""B""o""l""t""s""(""n""u""t""s"","" ""b""o""l""t""s"")""
"" "" "" "" ""a""s""s""e""r""t"" ""n""u""t""s"" ""=""="" ""[""'""a""'"","" ""'""b""'"","" ""'""d""'"","" ""'""g""'""]""
"" "" "" "" ""a""s""s""e""r""t"" ""b""o""l""t""s"" ""=""="" ""[""'""A""'"","" ""'""B""'"","" ""'""D""'"","" ""'""G""'""]