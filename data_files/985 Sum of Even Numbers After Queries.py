

from typing import List


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        
        cur_sum = sum(filter(lambda x: x % 2 == 0, A))
        ret = []
        for val, idx in queries:
            prev = A[idx]
            if prev % 2 == 0:
                cur_sum -= prev
            A[idx] += val
            if A[idx] % 2 == 0:
                cur_sum += A[idx]
            ret.append(cur_sum)

        return ret
