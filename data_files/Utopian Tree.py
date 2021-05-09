
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N = int(cipher[0])
        
        height = 1  
        for cycle in xrange(N):
            if cycle & 1 == 0:
                height *= 2
            else:
                height += 1

        return height


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
"" "" "" "" ""#"" ""f"" ""="" ""o""p""e""n""(