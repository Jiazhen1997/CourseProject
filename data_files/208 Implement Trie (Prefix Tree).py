
__author__ = 'Daniel'


class TrieNode:
    def __init__(self):
        
        self.ended = False
        self.children = {}


class Trie:
    def __init__(self):
        
        self.root = TrieNode()

    def insert(self, word):
        
        cur = self.root
        for w in word:
            if w not in cur.children:   
                cur.children[w] = TrieNode()
            cur = cur.children[w]

        cur.ended = True

    def search(self, word):
        
        cur = self.root
        for w in word:
            if w in cur.children:
                cur = cur.children[w]
            else:
                return False

        if not cur.ended:  
            return False

        return True

    def startsWith(self, prefix):
        
        cur = self.root
        for w in prefix:
            if w in cur.children:
                cur = cur.children[w]
            else:
                return False

        return True