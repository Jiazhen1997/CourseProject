
__author__ = 'Danyang'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root):
        
        result = []
        self.dfs(root, "","" ""r""e""s""u""l""t"")""
"" "" "" "" "" "" "" "" ""r""e""s""u""l""t"" ""="" ""[""i""n""t""(""e""l""e""m""e""n""t"")"" ""f""o""r"" ""e""l""e""m""e""n""t"" ""i""n"" ""r""e""s""u""l""t""]""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""u""m""(""r""e""s""u""l""t"")""
""
"" "" "" "" ""d""e""f"" ""d""f""s""(""s""e""l""f"","" ""r""o""o""t"","" ""c""u""r"","" ""r""e""s""u""l""t"")"":""
"" "" "" "" "" "" "" "" 
        if not root:
            return
        cur = cur+str(root.val)
        if not root.left and not root.right:
            result.append(cur)
            return

        if root.left:
            self.dfs(root.left, cur, result)
        if root.right:
            self.dfs(root.right, cur, result)


    def dfs_error(self, root, cur, result):
        
        if not root:
            return

        cur.append(root.val)

        if not root.left and not root.right:
            result.append(cur)
            return

        if root.left:
            self.dfs_error(root.left, cur, result)  
        if root.right:
            self.dfs_error(root.right, cur, result)


if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""n""o""d""e""s"" ""="" ""[""T""r""e""e""N""o""d""e""(""0"")"","" ""T""r""e""e""N""o""d""e""(""1"")"","" ""T""r""e""e""N""o""d""e""(""3"")""]""
"" "" "" "" ""n""o""d""e""s""[""0""]"".""l""e""f""t"" ""="" ""n""o""d""e""s""[""1""]""
"" "" "" "" ""n""o""d""e""s""[""0""]"".""r""i""g""h""t"" ""="" ""n""o""d""e""s""[""2""]""
"" "" "" "" ""S""o""l""u""t""i""o""n""("")"".""s""u""m""N""u""m""b""e""r""s""(""n""o""d""e""s""[""0""]"")