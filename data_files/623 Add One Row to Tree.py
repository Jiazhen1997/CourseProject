




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        return self.add(root, v, d, 1, "l"e"f"t"")""
""
"" "" "" "" ""d""e""f"" ""a""d""d""(""s""e""l""f"","" ""n""o""d""e"","" ""v"","" ""d"","" ""c""u""r""_""d"","" ""c""h""i""l""d"")"" ""-"">"" ""T""r""e""e""N""o""d""e"":""
"" "" "" "" "" "" "" "" ""#"" ""u""s""e"" ""t""h""e"" ""r""e""t""u""r""n"" ""v""a""l""u""e"" ""f""o""r"" ""p""a""r""e""n""t""'""s"" ""r""e""f""e""r""e""n""c""e"" ""
"" "" "" "" "" "" "" "" ""i""f"" ""c""u""r""_""d"" ""=""="" ""d"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""n""e""w"" ""="" ""T""r""e""e""N""o""d""e""(""v"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""t""a""t""t""r""(""n""e""w"","" ""c""h""i""l""d"","" ""n""o""d""e"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""n""e""w""
""
"" "" "" "" "" "" "" "" ""i""f"" ""n""o""d""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""n""o""d""e"".""l""e""f""t"" ""="" ""s""e""l""f"".""a""d""d""(""n""o""d""e"".""l""e""f""t"","" ""v"","" ""d"","" ""c""u""r""_""d"" ""+"" ""1"","" 