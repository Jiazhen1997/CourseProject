
__author__ = 'Daniel'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        
        if not root:
            return []

        ret = []
        self.dfs(root, [], ret)
        return ret

    def dfs(self, cur, path, ret):
        
        path.append(cur)
        if not cur.left and not cur.right:
            ret.append("-">"".""j""o""i""n""(""m""a""p""(""l""a""m""b""d""a"" ""x"":"" ""s""t""r""(""x"".""v""a""l"")"","" ""p""a""t""h"")"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n""
""
"" "" "" "" "" "" "" "" ""i""f"" ""c""u""r"".""l""e""f""t"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""f""s""(""c""u""r"".""l""e""f""t"","" ""p""a""t""h"","" ""r""e""t"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""p""a""t""h"".""p""o""p""("")"" "" ""#"" ""p""o""p"" ""t""h""e"" ""s""h""a""r""e""d"" ""p""a""t""h""
""
"" "" "" "" "" "" "" "" ""i""f"" ""c""u""r"".""r""i""g""h""t"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""f""s""(""c""u""r"".""r""i""g""h""t"","" ""p""a""t""h"","" ""r""e""t"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""p""a""t""h"".""p""o""p""("")"" "" ""#"" ""p""o""p"" ""t""h""e"" ""s""h""a""r""e""d"" ""p""a""t""h""
""
"" "" "" "" ""d""e""f"" ""d""f""s""_""p""a""t""h""(""s""e""l""f"","" ""c""u""r"","" ""p""a""t""h"","" ""r""e""t"")"":""
"" "" "" "" "" "" "" "" ""i""f"" ""n""o""t"" ""c""u""r"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n""
""
"" "" "" "" "" "" "" "" ""p""a""t""h"".""a""p""p""e""n""d""(""c""u""r"")""
"" "" "" "" "" "" "" "" ""i""f"" ""n""o""t"" ""c""u""r"".""l""e""f""t"" ""a""n""d"" ""n""o""t"" ""c""u""r"".""r""i""g""h""t"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t"".""a""p""p""e""n""d""(