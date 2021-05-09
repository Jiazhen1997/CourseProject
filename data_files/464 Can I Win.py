



class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        
        cache = {}
        
        choices = frozenset([choice for choice in range(1, maxChoosableInteger + 1)])
        return self._can_win(desiredTotal, choices, sum(choices), cache)

    def _can_win(self, total, choices, gross,cache):
        if (total, choices) in cache:
            return cache[(total, choices)]

        ret = False
        if max(choices) >= total:
            ret = True

        elif gross < total:
            ret = False
        else:
            for choice in choices:
                if not self._can_win(
                        total - choice,
                        choices - set([choice]),
                        gross - choice,
                        cache
                ):
                    ret = True
                    break

        cache[(total, choices)] = ret
        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""n""I""W""i""n""(""1""0"","" ""1""1"")"" ""=""="" ""F""a""l""s""e""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""n""I""W""i""n""(""1""0"","" ""0"")"" ""=""="" ""T""r""u""e""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""n""I""W""i""n""(""1""3"","" ""1""1"")"" ""=""="" ""T""r""u""e""
