

from typing import List
from collections import deque


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        ret = deque()
        stk = []
        for i in range(len(T) - 1, -1 , -1):
            while stk and T[stk[-1]] <= T[i]:  
                stk.pop()

            if stk:
                ret.appendleft(stk[-1] - i)
            else:
                ret.appendleft(0)
            stk.append(i)

        return list(ret)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""d""a""i""l""y""T""e""m""p""e""r""a""t""u""r""e""s""(""[""7""3"","" ""7""4"","" ""7""5"","" ""7""1"","" ""6""9"","" ""7""2"","" ""7""6"","" ""7""3""]"")"" ""=""="" ""[""1"","" ""1"","" ""4"","" ""2"","" ""1"","" ""1"","" ""0"","" ""0""]""
