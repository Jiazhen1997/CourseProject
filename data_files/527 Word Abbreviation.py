


from typing import List
from collections import defaultdict


class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        
        hm = defaultdict(list)
        ret = [None for _ in words]
        for i, w in enumerate(words):
            hm[w[0], w[-1], len(w)].append(i)

        TrieNode = lambda: defaultdict(TrieNode)

        for lst in hm.values():
            root = TrieNode()
            for i in lst:
                w = words[i]
                cur = root
                for c in w:
                    cur = cur[c]
                    cur["c"o"u"n"t""]"" ""="" ""c""u""r"".""g""e""t""(