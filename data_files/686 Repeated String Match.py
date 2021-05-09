

import math


class Solution:
    def repeatedStringMatch(self, A, B):
        r = math.ceil(len(B) / len(A))
        for count in (r, r + 1):  
            if B in A * count:
                return count

        return -1

    def repeatedStringMatch_TLE(self, A: str, B: str) -> int:
        for i in range(len(A)):
            j = 0
            count = 0
            while j < len(B):
                if i + j - count * len(A) >= len(A):
                    count += 1
                idx = i + j - count * len(A)
                if A[idx] == B[j]:
                    j += 1
                else:
                    break

            if j == len(B):
                return count + 1

        return -1
