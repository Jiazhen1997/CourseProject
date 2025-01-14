
from collections import defaultdict


__author__ = 'Daniel'


class Solution(object):
    def generatePalindromes(self, s):
        
        m = defaultdict(int)
        for c in s:
            m[c] += 1

        odd = None
        for k, v in m.items():
            if v % 2 == 1:
                if odd is not None:
                    return []
                odd = k

        cur = ""
"" "" "" "" "" "" "" "" ""i""f"" ""o""d""d"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""m""[""o""d""d""]"" ""-""="" ""1""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""u""r"" ""="" ""o""d""d""
""
"" "" "" "" "" "" "" "" ""r""e""t"" ""="" ""[""]""
"" "" "" "" "" "" "" "" ""#"" ""a""c""t""u""a""l""l""y"" ""o""n""l""y"" ""n""e""e""d"" ""t""o"" ""b""u""i""l""d"" ""h""a""l""f""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""g""r""o""w""(""s"","" ""m"","" ""N""o""n""e"","" ""c""u""r"","" ""r""e""t"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""r""e""t""
""
"" "" "" "" ""d""e""f"" ""g""r""o""w""(""s""e""l""f"","" ""s"","" ""c""o""u""n""t""_""m""a""p"","" ""p""i"","" ""c""u""r"","" ""r""e""t"")"":""
"" "" "" "" "" "" "" "" ""i""f"" ""l""e""n""(""c""u""r"")"" ""=""="" ""l""e""n""(""s"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t"".""a""p""p""e""n""d""(""c""u""r"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n""
""
"" "" "" "" "" "" "" "" ""f""o""r"" ""k"" ""i""n"" ""c""o""u""n""t""_""m""a""p"".""k""e""y""s""("")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""k"" ""!""="" ""p""i"" ""a""n""d"" ""c""o""u""n""t""_""m""a""p""[""k""]"" "">"" ""0"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""1"","" ""c""o""u""n""t""_""m""a""p""[""k""]""/""2""+""1"")"":"" "" ""#"" ""j""u""m""p"" ""t""h""e"" ""p""a""r""e""n""t""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""o""u""n""t""_""m""a""p""[""k""]"" ""-""="" ""i""*""2""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""g""r""o""w""(""s"","" ""c""o""u""n""t""_""m""a""p"","" ""k"","" ""k""*""i""+""c""u""r""+""k""*""i"","" ""r""e""t"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""o""u""n""t""_""m""a""p""[""k""]"" ""+""="" ""i""*""2""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 