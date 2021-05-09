
__author__ = 'Danyang'


class Solution:
    def singleNumber_optimal(self, A):
        
        bit_0, bit_1, bit_2 = ~0, 0, 0  
        for elmt in A:
            bit_t = bit_2  
            bit_2 = (bit_1 & elmt) | (bit_2 & ~elmt)
            bit_1 = (bit_0 & elmt) | (bit_1 & ~elmt)
            bit_0 = (bit_t & elmt) | (bit_0 & ~elmt)  
        return bit_1

    def singleNumber_array(self, A):
        
        cnt = [0 for _ in xrange(32)]

        for elmt in A:
            for i in xrange(32):
                if elmt>>i&1==1:
                    cnt[i] = (cnt[i]+1)%3

        result = 0
        for i in xrange(32):
            result |= cnt[i]<<i

        return result


    def singleNumber(self, A):
        
        one, two, three = 0, 0, 0

        
        
        
        
        
        

        for elmt in A:
            
            two |= one&elmt
            one ^= elmt
            three = one&two

            one &= ~three
            two &= ~three
        return one






if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""#"" ""p""o""s""s""i""b""l""e"" ""n""e""g""a""t""i""v""e"" ""n""u""m""b""e""r""s""
"" "" "" "" ""t""e""s""t""s"" ""="" ""[""
"" "" "" "" "" "" "" "" ""[""1"","" ""1"","" ""1"","" ""2"","" ""2"","" ""2"","" ""3"","" ""4"","" ""4"","" ""4""]"",""
"" "" "" "" "" "" "" "" ""[""1""]""
"" "" "" "" ""]""
"" "" "" "" ""f""o""r"" ""A"" ""i""n"" ""t""e""s""t""s"":""
"" "" "" "" "" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""s""i""n""g""l""e""N""u""m""b""e""r""_""o""p""t""i""m""a""l""(""A"")""=""=""S""o""l""u""t""i""o""n""("")"".""s""i""n""g""l""e""N""u""m""b""e""r""_""a""r""r""a""y""(""A"")""
"" "" "" "" "" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""s""i""n""g""l""e""N""u""m""b""e""r""_""o""p""t""i""m""a""l""(""A"")""=""=""S""o""l""u""t""i""o""n""("")"".""s""i""n""g""l""e""N""u""m""b""e""r""(""A"")""
