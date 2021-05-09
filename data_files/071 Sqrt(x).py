
__author__ = 'Danyang'
class Solution:
    def sqrt(self, x):
        
        if x==0: return 0  
        m = x
        while True:
            m_before = m
            m = m - float(m*m-x)/(2*m)
            if abs(m-m_before)<1e-7: break

        return int(m)

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""s""q""r""t""(""2"")