__author__ = 'Danyang'


class Solution:
    def generateParenthesisDfs(self, result, cur, left, right):
        
        
        if left==0 and right==0:
            result.append(cur)
            return
            
        if left>0:
            self.generateParenthesisDfs(result, cur+"("","" ""l""e""f""t""-""1"","" ""r""i""g""h""t"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""#"" ""a""d""d"" ""r""i""g""h""t"" ""p""a""r""e""n""t""h""e""s""i""s""
"" "" "" "" "" "" "" "" ""i""f"" ""r""i""g""h""t"">""l""e""f""t"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""g""e""n""e""r""a""t""e""P""a""r""e""n""t""h""e""s""i""s""D""f""s""(""r""e""s""u""l""t"","" ""c""u""r""+
        number of unique binary search tree
        Catalan Number

        C_n = {2n\choose n} - {2n\choose n+1}
        Proof: http://en.wikipedia.org/wiki/Catalan_number
        :param n: integer
        :return: integer
        

        

        