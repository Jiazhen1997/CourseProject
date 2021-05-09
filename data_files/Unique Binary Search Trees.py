
__author__ = 'Daniel'


class Solution:
    def __init__(self):
        self.cache = {}

    def numTrees(self, n):
        return self.dfs(n)

    def dfs(self, n):
        if n not in self.cache:
            if n in (0, 1, 2):
                self.cache[n] = max(1, n)
            else:
                s = 0
                for i in xrange(1, n+1):
                    l = self.dfs(i-1)
                    r = self.dfs(n-i)
                    s += l*r  

                self.cache[n] = s

        return self.cache[n]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""n""u""m""T""r""e""e""s""(""3"")