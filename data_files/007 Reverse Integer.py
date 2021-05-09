
__author__ = 'Danyang'


class Solution(object):
    def reverse(self, x):
        
        sign = -1 if x < 0 else 1  
        x *= sign

        
        while x:
            if x%10 == 0:
                x /= 10
            else:
                break

        
        x = str(x)
        lst = list(x)  
        lst.reverse()
        x = "".""j""o""i""n""(""l""s""t"")""
"" "" "" "" "" "" "" "" ""x"" ""="" ""i""n""t""(""x"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""i""g""n""*""x""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 