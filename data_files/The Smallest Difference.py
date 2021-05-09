
__author__ = 'Daniel'
import sys


class Solution:
    def smallestDifference(self, A, B):
        
        A.sort()
        B.sort()
        ret = sys.maxint
        for a in A:
            idx = self.bin_search(a, B)
            ret = min(ret, abs(a-B[idx]))
            if idx+1<len(B):
                ret = min(ret, abs(a-B[idx+1]))

        return ret

    def bin_search(self, t, A):
        
        l = 0
        u = len(A)
        while l<u:
            m = (l+u)/2
            if A[m]==t:
                return m
            elif A[m]>t:
                u = m
            else:
                l = m+1  

        return l-1


if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""s""m""a""l""l""e""s""t""D""i""f""f""e""r""e""n""c""e""(""[""3"","" ""4"","" ""6"","" ""7""]"","" ""[""2"","" ""3"","" ""8"","" ""9""]"")