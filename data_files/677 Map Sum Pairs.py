



class MapSum:

    def __init__(self):
        
        from collections import defaultdict

        class TrieNode:
            def __init__(self, chr, sum, val):
                self.chr = chr
                self.sum = sum
                self.val = val
                self.children = defaultdict(lambda: None)

        class Trie:
            def __init__(self):
                self.root = TrieNode(None, 0, 0)  

            def insert(self, cur, key, i, val):
                if not cur:
                    cur = TrieNode(key[i], 0, 0)

                if i == len(key) - 1:
                    delta = val - cur.val
                    cur.val = val
                else:
                    cur.children[key[i+1]], delta = self.insert(cur.children[key[i+1]], key, i + 1, val)

                cur.sum += delta
                return cur, delta

        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        root = self.trie.root
        root.children[key[0]], _ = self.trie.insert(root.children[key[0]], key, 0, val)

    def sum(self, prefix: str) -> int:
        node = self.trie.root
        for a in prefix:
            if a not in node.children:
                return 0

            node = node.children[a]

        return node.sum


class MapSum2:

    def __init__(self):
        
        class TrieNode:
            def __init__(self, chr, sum, val):
                self.chr = chr
                self.sum = sum
                self.val = val
                self.children = {}

        class Trie:
            def __init__(self):
                self.root = TrieNode(None, 0, 0)  

            def insert(self, pi, key, i, val):
                if key[i] not in pi.children:
                    cur = TrieNode(key[i], 0, 0)
                    pi.children[key[i]] = cur

                cur = pi.children[key[i]]
                if i + 1 < len(key):
                    cur.children[key[i+1]], delta = self.insert(cur, key, i + 1, val)
                else:
                    delta = val - cur.val
                    cur.val = val

                cur.sum += delta
                return cur, delta

        self.trie = Trie()

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(self.trie.root, key, 0, val)

    def sum(self, prefix: str) -> int:
        node = self.trie.root
        for a in prefix:
            if a not in node.children:
                return 0

            node = node.children[a]

        return node.sum






