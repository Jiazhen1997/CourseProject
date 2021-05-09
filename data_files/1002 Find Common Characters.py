

import string

from typing import List
from collections import Counter


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        
        ret = []
        if not A:
            return ret
            
        counter = Counter(A[0])
        for a in A[1:]:
            cur = Counter(a)
            for c in string.ascii_lowercase:
                counter[c] = min(counter[c], cur[c])

        for c in string.ascii_lowercase:
            if counter[c] > 0:
                ret.extend([c] * counter[c])

        return ret
