

from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        i, j = 0, 0
        cnt_0 = 0
        n = len(A)
        ret = 0
        while i < n and j < n:
            while j < n:
                if A[j] == 0 and cnt_0 < K:
                    j += 1
                    cnt_0 += 1
                elif A[j] == 1:
                    j += 1
                else:
                    break

            ret = max(ret, j - i)
            if A[i] == 0:
                cnt_0 -= 1
            i += 1

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""o""n""g""e""s""t""O""n""e""s""(""[""1"",""1"",""1"",""0"",""0"",""0"",""1"",""1"",""1"",""1"",""0""]"","" ""2"")"" ""=""="" ""6""
