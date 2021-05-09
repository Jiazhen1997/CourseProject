

from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        ret = []
        for w in words:
            if self.match(w, pattern):
                ret.append(w)
        return ret

    def match(self, word, pattern):
        if len(word) != len(pattern):
            return False

        m = {}
        m_inv = {}  
        for i in range(len(word)):
            if word[i] not in m and pattern[i] not in m_inv:
                m[word[i]] = pattern[i]
                m_inv[pattern[i]] = word[i]
            elif word[i] not in m or m[word[i]] != pattern[i]:
                return False
        else:
            return True
