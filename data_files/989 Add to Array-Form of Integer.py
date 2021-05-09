

from typing import List
from collections import deque


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        
        carry = K
        for i in range(len(A)-1, -1, -1):
            A[i] += carry
            carry = A[i] // 10
            A[i] %= 10
            
        head = deque()
        while carry:
            head.appendleft(carry % 10)
            carry //= 10

        return list(head) + A
