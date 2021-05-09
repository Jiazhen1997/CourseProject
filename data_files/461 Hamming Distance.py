



class Solution:
    def hammingDistance(self, x, y):
        
        diff = x ^ y
        ret = 0
        while diff:
            ret += diff & 1
            diff >>= 1
            
        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""h""a""m""m""i""n""g""D""i""s""t""a""n""c""e""(""3"","" ""1"")"" ""=""="" ""1""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""h""a""m""m""i""n""g""D""i""s""t""a""n""c""e""(""1"","" ""4"")"" ""=""="" ""2""
