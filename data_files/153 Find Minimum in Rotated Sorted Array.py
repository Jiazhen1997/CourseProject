
import sys

__author__ = 'Danyang'


class Solution(object):
    def findMin(self, A):
        
        lo = 0
        hi = len(A)
        mini = sys.maxint
        while lo < hi:
            mid = (lo+hi)/2
            mini = min(mini, A[mid])
            if A[lo] <= A[mid] <= A[hi-1]:
                return min(mini, A[lo])
            elif A[lo] > A[mid] < A[hi-1]:
                hi = mid
            else:
                lo = mid+1

        return mini


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""n""u""m"" ""="" ""[""7"","" ""1"","" ""2"","" ""3"","" ""4"","" ""5"","" ""6""]""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""M""i""n""(""n""u""m"")"" ""=""="" ""1""
