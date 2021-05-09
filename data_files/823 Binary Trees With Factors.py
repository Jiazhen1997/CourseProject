

from typing import List


MOD =  10 ** 9 + 7


class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        
        A.sort()
        F = {}
        for i in range(len(A)):
            F[A[i]] = 1
            for j in range(i):
                if A[i] % A[j] == 0 and A[i] // A[j] in F:
                    F[A[i]] += F[A[j]] * F[A[i] // A[j]]  
                    F[A[i]] %= MOD

        return sum(F.values()) % MOD
