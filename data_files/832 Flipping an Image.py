

from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
        for row in A:
            prev = list(row)
            for i in range(len(row)):
                row[i] = prev[-1-i] ^ 1

        return A
