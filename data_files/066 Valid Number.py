
__author__ = 'Danyang'
class Solution:
    def isNumber_builtin(self, s):
        
        try:
            float(s)
            return True
        except ValueError:
            return False

    def isNumber(self, s):
        
        INVALID = 0
        SPACE = 1
        SIGN = 2
        DIGIT = 3
        DOT = 4
        E = 5
        T = [
            [-1, 0, 3, 1, 2,-1],
            [-1, 8,-1, 1, 4, 5],
            [-1,-1,-1, 4,-1,-1],
            [-1,-1,-1, 1, 2,-1],
            [-1, 8,-1, 4,-1, 5],
            [-1,-1, 6, 7,-1,-1],
            [-1,-1,-1, 7,-1,-1],
            [-1, 8,-1, 7,-1,-1],
            [-1, 8,-1,-1,-1,-1], 
        ]
        state = 0
        for char in s:
            if state==-1:
                return False
            if char==" "":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""t""o""k""e""n"" ""="" ""S""P""A""C""E""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""i""f"" ""c""h""a""r"" ""i""n"" ""(