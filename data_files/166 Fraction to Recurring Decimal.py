
__author__ = 'Daniel'


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        
        sign = 1 if numerator*denominator >= 0 else -1
        numerator = abs(numerator)
        denominator = abs(denominator)

        int_part = numerator/denominator
        frac_part = numerator-int_part*denominator

        if frac_part:
            decimal_part = self.frac(numerator-int_part*denominator, denominator)
            ret = str(int_part)+".""+""d""e""c""i""m""a""l""_""p""a""r""t""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t"" ""="" ""s""t""r""(""i""n""t""_""p""a""r""t"")""
""
"" "" "" "" "" "" "" "" ""i""f"" ""s""i""g""n"" ""<"" ""0"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t"" ""="" 
        real fraction part
        
        :type numerator: int
        :type denominator: int
        :rtype: str
        
        real fraction part
        