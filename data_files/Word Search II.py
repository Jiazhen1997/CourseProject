
__author__ = 'Danyang'


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
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def wordSearchII_TLE(self, board, words):
        
        trie = Trie()
        for word in words:
            trie.add(word)

        ret = set()
        visited = set()
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                self.dfs(board, i, j, trie.root, visited, ret)

        return list(ret)

    def dfs(self, board, i, j, parent, visited, ret):
        
        c = board[i][j]
        visited.add((i, j))
        if c in parent.children:
            cur = parent.children[c]
            if cur.word:
                ret.add(cur.word)
            for direction in Solution.directions:
                row = i+direction[0]
                col = j+direction[1]
                if 0 <= row < len(board) and 0 <= col < len(board[0]) and (row, col) not in visited:
                    self.dfs(board, row, col, cur, visited, ret)
        visited.remove((i, j))

    def wordSearchII(self, board, words):
        
        ret = []
        for word in words:
            trie = Trie()
            trie.add(word)
            visited = set()
            r = set()
            found = False
            for i in xrange(len(board)):
                if not found:
                    for j in xrange(len(board[0])):
                        self.dfs2(board, i, j, trie.root, visited, r)
                        if len(r) == 1:  
                            ret.append(r.pop())
                            found = True
                            break

        return ret

    def dfs2(self, board, i, j, parent, visited, ret):
        
        c = board[i][j]
        visited.add((i, j))
        if c in parent.children:
            cur = parent.children[c]
            if cur.word:
                ret.add(cur.word)
            for direction in Solution.directions:
                row = i+direction[0]
                col = j+direction[1]
                if 0 <= row < len(board) and 0 <= col < len(board[0]) and (row, col) not in visited and not ret:
                    self.dfs2(board, row, col, cur, visited, ret)
        visited.remove((i, j))


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""b""o""a""r""d"" ""="" ""[