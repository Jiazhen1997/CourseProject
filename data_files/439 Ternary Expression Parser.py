



class Solution:
    def parseTernary(self, expression: str) -> str:
        
        stk = []
        for c in reversed(expression):
            if stk and stk[-1] == "?"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""t""k"".""p""o""p""("")"" "" ""#"" ""?""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""i""r""s""t"" ""="" ""s""t""k"".""p""o""p""("")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""t""k"".""p""o""p""("")"" "" ""#"" "":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""c""o""n""d"" ""="" ""s""t""k"".""p""o""p""("")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""c"" ""=""="" 
        tokenize + recursive (dfs)?

        stk from right to left, only include the operand

        can handle multiple digit (not required)
        