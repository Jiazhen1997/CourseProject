
__author__ = 'Daniel'


class Solution(object):
    def minAbbreviation(self, target, dictionary):
        
        ret = (target, len(target))
        for abbr, abbr_l in self.dfs(target):
            if self.validate(dictionary, abbr) and ret[1] > abbr_l:
                ret = (abbr, abbr_l)

        return ret[0]

    def dfs(self, word):
        
        if not word:
            return [("","" ""0"")""]""
""
"" "" "" "" "" "" "" "" ""r""e""t"" ""="" ""[""]""
"" "" "" "" "" "" "" "" ""f""o""r"" ""l"" ""i""n"" ""x""r""a""n""g""e""(""l""e""n""(""w""o""r""d"")""+""1"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""e""f""t""_""n""u""m"" ""="" ""s""t""r""(""l"")"" ""i""f"" ""l"" ""e""l""s""e"" 
        pointers
        :type word: str
        :type abbr: str
        :rtype: bool
        