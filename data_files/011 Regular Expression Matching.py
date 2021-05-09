
__author__ = 'Danyang'


class Solution:
    def isMatch_error(self, s, p):
        
        
        tape = s
        regex = p

        index = 0
        state = 0
        while index < len(tape) and state < len(regex):
            char = tape[index]
            if state+1 < len(regex) and regex[state+1] == "*"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""r""e""g""e""x""[""s""t""a""t""e""]"" ""!""="" 
        Algorithm: dfs, advancing the tape
        "."" ""i""s"" ""n""o""t"" ""a"" ""p""r""o""b""l""e""m""
"" "" "" "" "" "" "" "" 
        
        tape = s
        regex = p

        index = 0
        state = 0

        
        if not tape and not regex:
            return True
        
        if tape and not regex:  
            return False

        if not tape and regex:
            if state+1 < len(regex) and regex[state+1] == "*"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""i""s""M""a""t""c""h""(""t""a""p""e"","" ""r""e""g""e""x""[""s""t""a""t""e""+""2"":""]"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""F""a""l""s""e""
""
"" "" "" "" "" "" "" "" ""i""f"" ""s""t""a""t""e""+""1"" ""<"" ""l""e""n""(""r""e""g""e""x"")"" ""a""n""d"" ""r""e""g""e""x""[""s""t""a""t""e""+""1""]"" ""=""="" 
        Algorithm: dfs, advancing the tape  --> dp

        dp, similar to the dfs solution
        backward dp

          . * a * a -
        b
        b
        b
        b
        a
        -

        define dp[i][j] = tape[i:] and regex[j:] are matched
        So what is the state and how is the state transferred?
        :param s:
        :param p:
        :return: boolean
        