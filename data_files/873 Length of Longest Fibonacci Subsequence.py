

from typing import List


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
            
            n = len(A)
            F = [[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                F[i][i] = 1
                for j in range(i):
                    F[i][j] = 2

            idxes = {}
            for i in range(n):
                idxes[A[i]] = i

            for i in range(n):
                for j in range(i):
                    Ak = A[i] + A[j]
                    if Ak in idxes:
                        k = idxes[Ak]
                        F[k][i] = max(F[k][i], F[i][j] + 1)

            return max(
                F[i][j] if F[i][j] > 2 else 0
                for i in range(n)
                for j in range(i)
            )

    def lenLongestFibSubseq_TLE(self, A: List[int]) -> int:
        
        n = len(A)
        F = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            F[i][i] = 1
            for j in range(i):
                F[i][j] = 2

        for k in range(n):
            for i in range(k):
                for j in range(i):
                    if A[i] + A[j] == A[k]:
                        F[k][i] = max(F[k][i], F[i][j] + 1)

        return max(
            F[i][j] if F[i][j] > 2 else 0
            for i in range(n)
            for j in range(i)
        )

if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""e""n""L""o""n""g""e""s""t""F""i""b""S""u""b""s""e""q""(""[""1"",""2"",""3"",""4"",""5"",""6"",""7"",""8""]"")"" ""=""="" ""5""
