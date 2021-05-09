
__author__ = 'Danyang'
fib = lambda n: reduce(lambda x, n: [x[1], x[0] + x[1]], xrange(n), [0, 1])[0]


class Solution(object):
    def solve(self, cipher):
        
        num = int(cipher)
        n = 0
        while fib(n) < num:
            n += 1
        if fib(n) == num:
            return "I"s"F"i"b"o""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 