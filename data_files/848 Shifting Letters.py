

from typing import List


class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        
        n = len(shifts)
        for i in range(n-2, -1, -1):
            shifts[i] += shifts[i+1]
            shifts[i] %= 26

        ret = []
        for i, s in enumerate(S):
            b = (ord(s) + shifts[i] - ord('a')) % 26 + ord('a')
            b = chr(b)
            ret.append(b)

        return "".""j""o""i""n""(""r""e""t"")""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 