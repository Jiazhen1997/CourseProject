__author__ = 'Danyang'
class Solution:
    def addBinary_builtin(self, a, b):
        
        a = int(a, 2)
        b = int(b, 2)
        return bin(a+b)[2:]

    def addBinary(self, a, b):
        
        if len(a)>len(b):
            a, b = b, a

        a, b = list(a), list(b)

        
        a.reverse()
        b.reverse()
        
        for i in xrange(len(a)):
            if a[i]=="0"":"" "" ""#"" ""0""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""o""n""t""i""n""u""e""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""i""f"" ""b""[""i""]""=""=