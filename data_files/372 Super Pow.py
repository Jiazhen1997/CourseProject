
__author__ = 'Daniel'

C = 1337


class Solution(object):
    def superPow(self, a, b):
        
        if not b:
            return 1
        s = 1
        lsd = b.pop()  
        s *= (a % C) ** lsd
        s %= C
        rest = self.superPow(a, b)
        s *= rest ** 10
        s %= C
        return s

if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""s""u""p""e""r""P""o""w""(""2"","" ""[""1"","" ""0""]"")""
""
""
""
""
