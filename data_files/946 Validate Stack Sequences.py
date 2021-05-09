

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        j = 0
        n = len(pushed)
        stk = []
        for i in range(n):
            stk.append(pushed[i])
            while j < n and stk and stk[-1] == popped[j]:
                stk.pop()
                j += 1

        return j == n

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        i = 0
        j = 0
        stk = []
        n = len(pushed)
        while i < n and j < n:
            while i < n and (not stk or stk[-1] != popped[j]):
                stk.append(pushed[i])
                i += 1

            stk.pop()
            j += 1

        while j < n and stk and stk[-1] == popped[j]:
            stk.pop()
            j += 1

        return not stk
