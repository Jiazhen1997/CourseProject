

from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        
        ret = 0
        up_cnt = 0
        down_cnt = 0
        for i in range(1, len(A)):
            if down_cnt and A[i] >= A[i-1]:
                up_cnt = 0
                down_cnt = 0
            if A[i] > A[i-1]:
                up_cnt += 1
            elif A[i] < A[i-1]:
                down_cnt += 1
            if up_cnt and down_cnt:
                ret = max(ret, up_cnt + down_cnt + 1)

        return ret

    def longestMountain(self, A: List[int]) -> int:
        
        n = len(A)
        U = [0 for _ in A]  
        D = [0 for _ in A]  
        for i in range(1, n):
            if A[i] > A[i-1]:
                U[i] = U[i-1] + 1
        for i in range(n-2, -1, -1):
            if A[i] > A[i+1]:
                D[i] = D[i+1] + 1

        ret = 0
        for i in range(n):
            if U[i] > 0 and D[i] > 0:
                ret = max(ret, U[i] + D[i] + 1)

        return ret

    def longestMountain_complicated(self, A: List[int]) -> int:
        
        ret = 0
        l = 1
        expect_incr = True
        for i in range(1, len(A)):
            if expect_incr:
                if A[i] > A[i-1]:
                    l += 1
                elif A[i] < A[i-1] and l >= 2:
                    expect_incr = False
                    l += 1
                    ret = max(ret, l)
                else:
                    l = 1

            else:
                if A[i] < A[i-1]:
                    l += 1
                    ret = max(ret, l)
                elif A[i] == A[i-1]:
                    expect_incr = True
                    l = 1
                else:
                    expect_incr = True
                    l = 2

        return ret if ret >= 3 else 0


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""o""n""g""e""s""t""M""o""u""n""t""a""i""n""(""[""2"",""1"",""4"",""7"",""3"",""2"",""5""]"")"" ""=""="" ""5""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""o""n""g""e""s""t""M""o""u""n""t""a""i""n""(""[""9"",""8"",""7"",""6"",""5"",""4"",""3"",""2"",""1"",""0""]"")"" ""=""="" ""0""
