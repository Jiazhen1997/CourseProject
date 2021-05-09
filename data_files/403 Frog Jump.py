
__author__ = 'Daniel'


class Solution(object):
    def canCross(self, stones):
        
        F = {}
        for stone in stones:
            F[stone] = set()

        F[0].add(0)
        for stone in stones:
            for step in F[stone]:
                for i in (-1, 0, 1):
                    nxt = stone + step + i
                    if nxt != stone and nxt in F:
                        F[nxt].add(step + i)

        return True if F[stones[-1]] else False


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""n""C""r""o""s""s""(""[""0"","" ""2""]"")"" ""=""="" ""F""a""l""s""e""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""n""C""r""o""s""s""(""[""0"","" ""1"","" ""3"","" ""5"","" ""6"","" ""8"","" ""1""2"","" ""1""7""]"")"" ""=""="" ""T""r""u""e""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""n""C""r""o""s""s""(""[""0"","" ""1"","" ""2"","" ""3"","" ""4"","" ""8"","" ""9"","" ""1""1""]"")"" ""=""="" ""F""a""l""s""e""
