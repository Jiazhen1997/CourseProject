
__author__ = 'Danyang'
class Solution:
    def generateParenthesis(self, n):
        
        result = []
        self.generateParenthesisDfs(result, "","" ""n"","" ""n"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""r""e""s""u""l""t""
""
"" "" "" "" ""d""e""f"" ""g""e""n""e""r""a""t""e""P""a""r""e""n""t""h""e""s""i""s""D""f""s""(""s""e""l""f"","" ""r""e""s""u""l""t"","" ""c""u""r"","" ""l""e""f""t"","" ""r""i""g""h""t"")"":""
"" "" "" "" "" "" "" "" 
        if left == 0 and right == 0:
            result.append(cur)
            return

        
        if left > 0:
            self.generateParenthesisDfs(result, cur + "("","" ""l""e""f""t"" ""-"" ""1"","" ""r""i""g""h""t"")""
"" "" "" "" "" "" "" "" ""#"" ""a""d""d"" ""r""i""g""h""t"" ""p""a""r""e""n""t""h""e""s""i""s""
"" "" "" "" "" "" "" "" ""i""f"" ""r""i""g""h""t"" "">"" ""l""e""f""t"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""g""e""n""e""r""a""t""e""P""a""r""e""n""t""h""e""s""i""s""D""f""s""(""r""e""s""u""l""t"","" ""c""u""r"" ""+"" 