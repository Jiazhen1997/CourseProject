

from typing import List


class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        i = 0
        j = 0
        ret = []
        n = len(S)
        while j < n:
            while j < n and S[i] == S[j]:
                j += 1
            if j - i >= 3:
                ret.append([i, j - 1])
            i = j

        return ret 
