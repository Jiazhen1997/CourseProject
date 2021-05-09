




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import OrderedDict


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        
        depth = 0
        
        n = len(S)
        i = 0
        root = None
        stk = []
        while i < n:
            if S[i] == "-"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""d""e""p""t""h"" ""+""="" ""1""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i"" ""+""="" ""1""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""j"" ""="" ""i""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""w""h""i""l""e"" ""j"" ""<"" ""n"" ""a""n""d"" ""S""[""j""]"" ""!""="" 
        map: node -> depth
        stack of pi (incompleted)
        