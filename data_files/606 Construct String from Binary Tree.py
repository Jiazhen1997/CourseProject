



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ""
""
"" "" "" "" "" "" "" "" ""l""e""f""t"" ""="" ""s""e""l""f"".""t""r""e""e""2""s""t""r""(""t"".""l""e""f""t"")""
"" "" "" "" "" "" "" "" ""r""i""g""h""t"" ""="" ""s""e""l""f"".""t""r""e""e""2""s""t""r""(""t"".""r""i""g""h""t"")""
"" "" "" "" "" "" "" "" ""r""e""t"" ""="" ""[""s""t""r""(""t"".""v""a""l"")""]""
"" "" "" "" "" "" "" "" ""i""f"" ""l""e""f""t"" ""o""r"" ""r""i""g""h""t"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t"".""a""p""p""e""n""d""(