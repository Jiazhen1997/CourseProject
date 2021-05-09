



class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last = None
        while n:
            cur = n & 1
            
            if last is not None and last ^ cur == 0:
                return False
            last = cur
            n >>= 1

        return True


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""h""a""s""A""l""t""e""r""n""a""t""i""n""g""B""i""t""s""(""5"")"" ""=""="" ""T""r""u""e""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""h""a""s""A""l""t""e""r""n""a""t""i""n""g""B""i""t""s""(""7"")"" ""=""="" ""F""a""l""s""e""
