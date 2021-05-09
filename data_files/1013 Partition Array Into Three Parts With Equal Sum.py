

from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False

        target = s // 3
        count = 0
        cur_sum = 0
        for a in A:
            cur_sum += a
            if cur_sum == target:
                count += 1
                cur_sum = 0
            
            
            

        return count == 3 and cur_sum == 0


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""n""T""h""r""e""e""P""a""r""t""s""E""q""u""a""l""S""u""m""(""[""3"",""3"",""6"",""5"",""-""2"",""2"",""5"",""1"",""-""9"",""4""]"")"" ""=""="" ""T""r""u""e""
