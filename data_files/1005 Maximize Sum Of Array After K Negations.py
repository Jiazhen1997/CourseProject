

from typing import List


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        
        A.sort()
        for i in range(len(A)):
            if K == 0:
                break

            if A[i] < 0:
                A[i] *= -1
                prev = A[i]
                K -= 1
            else:
                if K % 2 != 0:
                    if i - 1 >= 0 and A[i-1] < A[i]:
                        A[i-1] *= -1
                    else:
                        A[i] *= -1
                break

        return sum(A)
