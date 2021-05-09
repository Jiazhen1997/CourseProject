

from typing import List


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        
        flag = None  
        ret = 1
        cur = 1
        for i in range(len(A)-1):
            if A[i] == A[i+1]:
                flag = None
                cur = 1
            elif A[i] > A[i+1]:
                if flag is None or flag == 1:
                    cur += 1
                    ret = max(ret, cur)
                else:
                    cur = 2
                flag = 0
            else:  
                if flag is None or flag == 0:
                    cur += 1
                    ret = max(ret, cur)
                else:
                    cur = 2
                flag = 1

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""T""u""r""b""u""l""e""n""c""e""S""i""z""e""(""[""9"",""4"",""2"",""1""0"",""7"",""8"",""8"",""1"",""9""]"")"" ""=""="" ""5""
