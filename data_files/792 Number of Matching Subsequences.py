

from typing import List
from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        
        itrs_m = defaultdict(list)
        for w in words:
            itrs_m[w[0]].append(
                iter(w[1:])
            )
        for a in S:
            itrs = itrs_m.pop(a, [])
            for itr in itrs:
                v = next(itr, None)
                itrs_m[v].append(itr)

        return len(itrs_m[None])

    def numMatchingSubseq_TLE(self, S: str, words: List[str]) -> int:
        
        I = [0 for _ in words]
        for a in S:
            for wi, i in enumerate(I):
                if i < len(words[wi]) and words[wi][i] == a:
                    I[wi] += 1

        return sum(
            1
            for wi, i in enumerate(I)
            if i == len(words[wi])
        )


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""n""u""m""M""a""t""c""h""i""n""g""S""u""b""s""e""q""(