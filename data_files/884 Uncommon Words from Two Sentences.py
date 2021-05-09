

from typing import List
from collections import Counter


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        
        c = Counter(A.split()) + Counter(B.split())
        ret = [
            k
            for k, v in c.items()
            if v == 1
        ]
        return ret

    def uncommonFromSentences_complext(self, A: str, B: str) -> List[str]:
        
        c_A, c_B = Counter(A.split()), Counter(B.split())
        ret = []
        for k, v in c_A.items():
            if v == 1 and k not in c_B:
                ret.append(k)

        for k, v in c_B.items():
            if v == 1 and k not in c_A:
                ret.append(k)

        return ret

    def uncommonFromSentences_error(self, A: str, B: str) -> List[str]:
        
        s_A, s_B = set(A.split()), set(B.split())
        return list(
            (s_A - s_B) | (s_B - s_A)
        )
