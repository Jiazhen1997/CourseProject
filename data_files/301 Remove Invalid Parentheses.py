
__author__ = 'Daniel'


class Solution(object):
    def removeInvalidParentheses(self, s):
        
        rmcnt = self.minrm(s)
        ret = []
        self.dfs(s, "","" ""0"","" ""N""o""n""e"","" ""0"","" ""r""m""c""n""t"","" ""r""e""t"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""r""e""t""
""
"" "" "" "" ""d""e""f"" ""m""i""n""r""m""(""s""e""l""f"","" ""s"")"":""
"" "" "" "" "" "" "" "" 
        rmcnt = 0
        left = 0
        for c in s:
            if c == "("":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""l""e""f""t"" ""+""="" ""1""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""i""f"" ""c"" ""=""="" 
        Remove parenthesis
        backtracking, post-check
        :param s: original string
        :param cur: current string builder
        :param left: number of remaining left parentheses in s[0..i] not consumed by ")""
"" "" "" "" "" "" "" "" "":""p""a""r""a""m"" ""p""i"":"" ""l""a""s""t"" ""r""e""m""o""v""e""d"" ""c""h""a""r""
"" "" "" "" "" "" "" "" "":""p""a""r""a""m"" ""i"":"" ""c""u""r""r""e""n""t"" ""i""n""d""e""x""
"" "" "" "" "" "" "" "" "":""p""a""r""a""m"" ""r""m""c""n""t"":"" ""n""u""m""b""e""r"" ""o""f"" ""r""e""m""a""i""n""i""n""g"" ""r""e""m""o""v""a""l""s"" ""n""e""e""d""e""d""
"" "" "" "" "" "" "" "" "":""p""a""r""a""m"" ""r""e""t"":"" ""r""e""s""u""l""t""s""
"" "" "" "" "" "" "" "" 