
__author__ = 'Daniel'


class TrieNode(object):
    def __init__(self, char):
        self.char = char
        self.word = None
        self.children = {}  

    def __repr__(self):
        return repr(self.char)


class Trie(object):
    def __init__(self):
        self.root = TrieNode(None)

    def add(self, word):
        word = word.lower()
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]
        cur.word = word


class Solution:
    def __init__(self):
        self.dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def findWords(self, board, words):
        
        trie = Trie()
        for word in words:
            trie.add(word)

        ret = set()
        marked = set()
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, i, j, trie.root, marked, ret)

        return list(ret)

    def dfs(self, board, i, j, parent, marked, ret):
        
        m = len(board)
        n = len(board[0])
        marked.add((i, j))
        c = board[i][j]

        if c in parent.children:
            cur = parent.children[c]
            if cur.word:
                ret.add(cur.word)
            for dir in self.dirs:
                row = i+dir[0]
                col = j+dir[1]
                if 0 <= row < m and 0 <= col < n and (row, col) not in marked:
                    self.dfs(board, row, col, cur, marked, ret)

        marked.remove((i, j))