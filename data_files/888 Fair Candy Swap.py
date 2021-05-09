

from typing import List
import bisect


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        
        sum_A = sum(A)
        sum_B = sum(B)
        diff = (sum_B - sum_A) // 2  
        set_B = set(B)
        for a in A:
            if a + diff in set_B:
                return [a, a + diff]
                
        raise

    def fairCandySwap_complex(self, A: List[int], B: List[int]) -> List[int]:
        
        sum_A = sum(A)
        sum_B = sum(B)
        if sum_A > sum_B:
            return self.fairCandySwap(B, A)[::-1]

        A.sort()
        B.sort()
        diff = (sum_B - sum_A) // 2
        for a in A:
            i = bisect.bisect_left(B, a + diff)
            if i < len(B) and B[i] == a + diff:
                return [a, a + diff]

        raise
