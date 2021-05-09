

from typing import List
from collections import Counter


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        A.sort(key=abs)
        counter = Counter(A)
        for a in A:
            if counter[a] == 0:
                continue
            if counter[2*a] == 0:
                return False

            counter[a] -= 1
            counter[2*a] -= 1

        return True

    def canReorderDoubled_positive_negative(self, A: List[int]) -> bool:
        
        A.sort()
        counter = Counter(A)
        for a in A:
            if counter[a] == 0:
                continue
            counter[a] -= 1
            if a > 0:
                target = 2 * a
            elif a % 2 != 0:
                return False
            else:
                target = a // 2

            if counter[target] > 0:
                counter[target] -= 1
            else:
                return False

        return True


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""n""R""e""o""r""d""e""r""D""o""u""b""l""e""d""(""[""4"",""-""2"",""2"",""-""4""]"")"" ""=""="" ""T""r""u""e""
