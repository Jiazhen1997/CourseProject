

from collections import deque


class Solution:
    def baseNeg2(self, N: int) -> str:
        
        ret = deque()
        while N != 0:
            r = N % 2  
            ret.appendleft(r)
            N -= r
            N //= -2

        return "".""j""o""i""n""(""m""a""p""(""s""t""r"","" ""r""e""t"")"")"" ""o""r"" 