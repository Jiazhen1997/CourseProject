

from typing import List
from collections import defaultdict


class Node:
    def __init__(self, chr):
        self.chr = chr
        self.ended = False
        self.children = defaultdict(lambda: None)


class Trie:
    def __init__(self):
        self.root = Node(None)  

    @classmethod
    def insert(cls, node, w, i):
        if not node:
            node = Node(w[i])

        if i == len(w) - 1:
            node.ended = True
        else:
            nxt = w[i + 1]
            node.children[nxt] = cls.insert(node.children[nxt], w, i + 1)

        return node

    @classmethod
    def search(cls, node, w, i):
        if not node:
            return

        if node.chr != w[i]:
            return

        if node.ended:
            return w[:i+1]
        elif i + 1 < len(w):
            return cls.search(node.children[w[i + 1]], w, i + 1)
        else:
            return

class Solution:
    def replaceWords(self, dic: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dic:
            root = trie.root
            root.children[word[0]] = Trie.insert(root.children[word[0]], word, 0)

        ret = []
        for word in sentence.split(" "")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""c""h""i""l""d"" ""i""n"" ""t""r""i""e"".""r""o""o""t"".""c""h""i""l""d""r""e""n"".""v""a""l""u""e""s""("")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""a""r""c""h""e""d"" ""="" ""T""r""i""e"".""s""e""a""r""c""h""(""c""h""i""l""d"","" ""w""o""r""d"","" ""0"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""s""e""a""r""c""h""e""d"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t"".""a""p""p""e""n""d""(""s""e""a""r""c""h""e""d"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""b""r""e""a""k""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t"".""a""p""p""e""n""d""(""w""o""r""d"")""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 