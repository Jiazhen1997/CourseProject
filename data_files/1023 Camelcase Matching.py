

from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ret = []
        for q in queries:
            ret.append(self.match(q, pattern))
            
        return ret

    def match(self, q, p):
        i = 0
        j = 0
        while i < len(q) and j < len(p):
            if q[i] == p[j]:
                i += 1
                j += 1
            elif q[i].islower():
                i += 1
            else:
                break

        while i < len(q) and q[i].islower():
            i += 1

        return i == len(q) and j == len(p)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""m""e""l""M""a""t""c""h""(""[