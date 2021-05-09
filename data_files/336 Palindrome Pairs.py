

from typing import List
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.pali_prefix_idxes = []  
        self.word_idx = None
        self.children = defaultdict(TrieNode)


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        root = TrieNode()
        for idx, w in enumerate(words):
            cur = root
            for i in range(len(w) - 1, -1, -1):
                
                if self.is_palindrome(w, 0, i + 1):
                    cur.pali_prefix_idxes.append(idx)

                cur = cur.children[w[i]]

            cur.pali_prefix_idxes.append(idx)  
            cur.word_idx = idx  

        ret = []
        for idx, w in enumerate(words):
            cur = root
            for i in range(len(w)):
                
                if self.is_palindrome(w, i, len(w)) and cur.word_idx is not None and cur.word_idx != idx:
                    ret.append([idx, cur.word_idx])

                cur = cur.children.get(w[i], None)
                if cur is None:
                    break
            else:
                for idx_j in cur.pali_prefix_idxes:
                    if idx != idx_j:
                        ret.append([idx, idx_j])

        return ret

    def is_palindrome(self, w, lo, hi):
        i = lo
        j = hi - 1
        while i < j:
            if w[i] != w[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""p""a""l""i""n""d""r""o""m""e""P""a""i""r""s""(""[