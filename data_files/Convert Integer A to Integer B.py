
__author__ = 'Danyang'


class Solution:
    def bitSwapRequired(self, a, b):
        
        a = self.to_bin(a)
        b = self.to_bin(b)
        diff = len(a)-len(b)
        ret = 0
        if diff<0:
            a, b = b, a
            diff *= -1
        b = "0""*""d""i""f""f""+""b""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""l""e""n""(""b"")"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""a""[""i""]""!""=""b""[""i""]"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t"" ""+""="" ""1""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""r""e""t""
""
"" "" "" "" ""d""e""f"" ""t""o""_""b""i""n""(""s""e""l""f"","" ""n"")"":""
"" "" "" "" "" "" "" "" 
        
        a = abs(n)
        lst = []
        while a>0:
            lst.append(a%2)
            a /= 2

        
        if n>=0:
            lst.extend([0]*(32-len(lst)))
        else:
            pivot = -1
            for i in xrange(len(lst)):
                if pivot==-1 and lst[i]==1:
                    pivot = i
                    continue
                if pivot!=-1:
                    lst[i] ^= 1

            lst.extend([1]*(32-len(lst)))

        return "".""j""o""i""n""(""m""a""p""(""s""t""r"","" ""r""e""v""e""r""s""e""d""(""l""s""t"")"")"")""
""
""i""f"" ""_""_""n""a""m""e""_""_""=""=