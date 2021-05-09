

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ret = set()
        seen = set()
        for i in range(len(s) - 10 + 1):
            sub = s[i:i+10]
            if sub in seen and sub not in ret:
                ret.add(sub)
            else:
                seen.add(sub)

        return list(ret)
