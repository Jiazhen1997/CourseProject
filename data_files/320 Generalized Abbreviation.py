
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def generateAbbreviations(self, word):
        
        if not word:
            return [""]""
""
"" "" "" "" "" "" "" "" ""r""e""t"" ""="" ""[""]""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""l""e""n""(""w""o""r""d"")""+""1"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""e""f""t""_""n""u""m"" ""="" ""s""t""r""(""i"")"" ""i""f"" ""i"" ""e""l""s""e"" 
        Cached, brute force
        Two-way backtracking, pivoting number
        :type word: str
        :rtype: List[str]
        