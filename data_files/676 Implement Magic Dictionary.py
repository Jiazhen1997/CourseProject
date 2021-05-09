

from typing import List
from collections import defaultdict


class MagicDictionary:

    def __init__(self):
        
        class Node:
            def __init__(self, chr):
                self.chr = chr
                self.end = False  
                self.children = defaultdict(lambda: None)

        class Trie:
            def __init__(self):
                self.root = Node(None)

            def insert(self, cur, s, i):
                if not cur:
                    cur = Node(s[i])

                if i == len(s) -1:
                    cur.end = True
                else:
                    nxt = s[i+1]
                    cur.children[nxt] = self.insert(cur.children[nxt], s, i + 1)

                return cur

            def search(self, cur, s, i, modified):
                if cur.chr != s[i]:
                    if modified:
                        return False
                    modified = True

                if i == len(s) - 1:
                    
                    return modified and cur.end

                for child in cur.children.values():
                    if self.search(child, s, i + 1, modified):
                        return True

                return False

        self.trie = Trie()

    def buildDict(self, dic: List[str]) -> None:
        
        for s in dic:
            root = self.trie.root
            root.children[s[0]] = self.trie.insert(root.children[s[0]], s, 0)

    def search(self, word: str) -> bool:
        
        for child in self.trie.root.children.values():
            if self.trie.search(child, word, 0, False):
                return True

        return False






