
__author__ = 'Daniel'


class TrieNode:
    def __init__(self):
        
        
        self.ended = False
        self.children = {}


class WordDictionary:
    def __init__(self):
        
        self.root = TrieNode()

    def addWord(self, word):
        
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]

        cur.ended = True

    def search(self, word):
        
        return self.__search(word, self.root)

    def __search(self, word, cur):
        if not word:
            return cur.ended

        w = word[0]
        if w != "."":""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""w"" ""i""n"" ""c""u""r"".""c""h""i""l""d""r""e""n"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""_""_""s""e""a""r""c""h""(""w""o""r""d""[""1"":""]"","" ""c""u""r"".""c""h""i""l""d""r""e""n""[""w""]"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""F""a""l""s""e""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""c""h""i""l""d"" ""i""n"" ""c""u""r"".""c""h""i""l""d""r""e""n"".""v""a""l""u""e""s""("")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""s""e""l""f"".""_""_""s""e""a""r""c""h""(""w""o""r""d""[""1"":""]"","" ""c""h""i""l""d"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""T""r""u""e""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""F""a""l""s""e""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 