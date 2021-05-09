

from typing import List
from bisect import bisect_left
from collections import deque


class Solution:
    def findClosestElements(self, A: List[int], k: int, x: int) -> List[int]:
        
        n = len(A)
        lo = 0
        hi = n - k
        while lo < hi:
            mid = (lo + hi) // 2
            if abs(x - A[mid]) > abs(A[mid + k] - x):
                
                lo = mid + 1
            else:
                hi = mid

        return A[lo:lo+k]

    def findClosestElements2(self, A: List[int], k: int, x: int) -> List[int]:
        
        n = len(A)
        idx = bisect_left(A, x)
        ret = deque()
        i = idx - 1
        j = idx
        while k:
            if 0 <= i < n and 0 <= j < n:
                if abs(A[i] - x) <= abs(A[j] - x):
                    ret.appendleft(A[i])
                    i -= 1
                else:
                    ret.append(A[j])
                    j += 1
            elif 0 <= i < n:
                ret.appendleft(A[i])
                i -= 1
            elif 0 <= j < n:
                ret.append(A[j])
                j += 1
            else:
                raise

            k -= 1

        return list(ret)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""C""l""o""s""e""s""t""E""l""e""m""e""n""t""s""(""[""1"",""2"",""3"",""4"",""5""]"","" ""4"","" ""3"")"" ""=""="" ""[""1"",""2"",""3"",""4""]""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""C""l""o""s""e""s""t""E""l""e""m""e""n""t""s""(""[""1"",""2"",""3"",""4"",""5""]"","" ""4"","" ""-""1"")"" ""=""="" ""[""1"",""2"",""3"",""4""]""
