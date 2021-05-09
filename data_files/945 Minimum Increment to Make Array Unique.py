

from typing import List
from collections import Counter


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        
        if not A:
            return 0

        A.sort()
        ret = 0
        prev = A[0]
        for i in range(1, len(A)):
            target = prev + 1
            if A[i] < target:
                
                ret += target - A[i]
                prev = target 
            else:
                prev = A[i]
        return ret


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        
        counter = Counter(A)
        q = []
        ret = 0
        for i in range(40000 * 2):
            if counter[i] > 1:
                q.extend([i] * (counter[i] - 1))
            elif q and counter[i] == 0:
                ret += i - q.pop()
        return ret

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        
        ret = 0
        A.sort()
        A.append(1 << 31 - 1)  
        demand = 0
        supply = 0
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                demand += 1
                
                ret -= A[i-1]  
            else:
                supply = min(demand, A[i] - A[i-1] - 1)
                
                ret += (A[i-1] + 1 + A[i-1] + supply) * supply // 2
                demand -= supply

        return ret
