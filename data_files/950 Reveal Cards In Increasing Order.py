

from typing import List
from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        q = deque()
        deck.sort()
        for i in range(len(deck) - 1, -1, -1):
            if q:
                tail = q.pop()
                q.appendleft(tail)
            q.appendleft(deck[i])

        return list(q)
