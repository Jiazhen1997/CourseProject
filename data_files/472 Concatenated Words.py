

from typing import List
from collections import defaultdict


class Solution:
    def __init__(self):
        TrieNode = lambda: defaultdict(TrieNode)  
        self.root = TrieNode()  

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        words.sort(key=len)
        ret = []
        for w in words:
            if self.can_concat(w, 0):
                ret.append(w)

            cur = self.root
            for c in w:
                cur = cur[c]
            cur["e"n"d""]"" ""="" ""T""r""u""e""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""r""e""t""
""
"" "" "" "" ""d""e""f"" ""c""a""n""_""c""o""n""c""a""t""(""s""e""l""f"","" ""w""o""r""d"","" ""l""o"")"":""
"" "" "" "" "" "" "" "" ""i""f"" ""n""o""t"" ""w""o""r""d"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""F""a""l""s""e""
""
"" "" "" "" "" "" "" "" ""k"" ""="" ""l""e""n""(""w""o""r""d"")""
"" "" "" "" "" "" "" "" ""i""f"" ""l""o"" "">""="" ""k"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""T""r""u""e""
""
"" "" "" "" "" "" "" "" ""c""u""r"" ""="" ""s""e""l""f"".""r""o""o""t""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""g""e""(""l""o"","" ""k"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""u""r"" ""="" ""c""u""r""[""w""o""r""d""[""i""]""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""c""u""r"".""g""e""t""(
        Trie check cannot be greedy: cat sdog vs cats dog

        Sort + Trie dfs
        What is the complexity?

        Word break DP
        for a specific word
        F[i] means word[:i] can be formed using shorter words

        complexity
        O(n) * O(k^2) * O(k)
        n words * get F * compare words

        Hard question is solving a collections of medium problems
        