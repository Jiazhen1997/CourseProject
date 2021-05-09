
__author__ = 'Danyang'


class Solution:
    def updateBits(self, n, m, i, j):
        
        mask = ((1<<32)-1)-((1<<j+1)-1)+((1<<i)-1)
        ret = (n&mask)+(m<<i)
        return self.twos_comp(ret, 32)

    @staticmethod
    def twos_comp(val, bits):
        
        if val > 0 and val&(1<<(bits-1)) != 0:  
            val -= 1<<bits
        return val


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""u""p""d""a""t""e""B""i""t""s""(""-""2""1""4""7""4""8""3""6""4""8"","" ""2""1""4""7""4""8""3""6""4""7"","" ""0"","" ""3""0"")"" ""=""="" ""-""1""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""u""p""d""a""t""e""B""i""t""s""(""1"","" ""-""1"","" ""0"","" ""3""1"")"" ""=""="" ""-""1""
"" "" "" "" ""n"" ""="" ""i""n""t""(