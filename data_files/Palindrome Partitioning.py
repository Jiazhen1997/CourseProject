
__author__ = 'Daniel'


class Solution:
    def partition(self, s):
        
        ret = []
        self.backtrack(s, [], ret)
        return ret

    def backtrack(self, s, cur_lvl, ret):
        
        if not s:
            ret.append(list(cur_lvl))

        for i in xrange(1, len(s)+1):
            if self.predicate(s[:i]):
                cur_lvl.append(s[:i])
                self.backtrack(s[i:], cur_lvl, ret)
                cur_lvl.pop()

    def predicate(self, s):
        return s == s[::-1]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""p""a""r""t""i""t""i""o""n""(