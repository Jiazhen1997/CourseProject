

from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even_idx = 0
        for odd_idx in range(1, len(A), 2):
            if A[odd_idx] % 2 == 0:
                while A[even_idx] % 2 == 0:
                    even_idx += 2
                A[odd_idx], A[even_idx] = A[even_idx], A[odd_idx]

        return A

    def sortArrayByParityII_complex(self, A: List[int]) -> List[int]:
        
        closed = -1
        n = len(A)
        for i in range(n):
            if A[i] % 2 == 0:
                closed += 1
                A[i], A[closed] = A[closed], A[i]

        j = closed + 1
        if j % 2 == 1:
            j += 1
        for i in range(1, closed + 1, 2):
            A[i], A[j] = A[j], A[i]
            j += 2

        return A


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""s""o""r""t""A""r""r""a""y""B""y""P""a""r""i""t""y""I""I""(""[""4"",""1"",""1"",""0"",""1"",""0""]"")"" ""=""="" ""[""4"",""1"",""0"",""1"",""0"",""1""]""
