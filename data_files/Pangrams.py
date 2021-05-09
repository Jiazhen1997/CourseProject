
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        bucket = [False for _ in xrange(26)]
        for char in cipher:
            char = char.lower()
            ind = ord(char) - ord('a')
            try:
                bucket[ind] = True
            except IndexError:
                pass

        is_pangram = all(bucket)
        if is_pangram:
            return "p"a"n"g"r"a"m""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 