
__author__ = 'Danyang'


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        return repr(self.val)


class Solution:
    def lowestCommonAncestor(self, root, A, B):
        
        p1 = self.path(root, A)
        p2 = self.path(root, B)
        p1.append(TreeNode(0))  
        p2.append(TreeNode(0))  
        for ind, val in enumerate(p1):
            if val != p2[ind]:
                return p1[ind-1]

    def path(self, root, target):
        
        ans = []
        self.get_path(root, target, [], ans)
        return ans

    def get_path(self, cur, target, path, ans):
        
        if not cur:
            return False

        path.append(cur)

        if cur == target:  
            
            ans.extend(path)  
            return True

        if cur.left and self.get_path(cur.left, target, path, ans):
            return True

        if cur.right and self.get_path(cur.right, target, path, ans):
            return True

        path.pop()
        return False


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""n""o""d""e"" ""="" ""T""r""e""e""N""o""d""e""(""1"")""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""l""o""w""e""s""t""C""o""m""m""o""n""A""n""c""e""s""t""o""r""(""n""o""d""e"","" ""n""o""d""e"","" ""n""o""d""e"")""
""
"" "" "" "" ""n""o""d""e""s"" ""="" ""d""i""c""t""(""z""i""p""(""r""a""n""g""e""(""3"","" ""8"")"","" ""[""T""r""e""e""N""o""d""e""(""i"")"" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""g""e""(""3"","" ""8"")""]"")"")""
"" "" "" "" ""n""o""d""e""s""[""4""]"".""l""e""f""t"" ""="" ""n""o""d""e""s""[""3""]""
"" "" "" "" ""n""o""d""e""s""[""4""]"".""r""i""g""h""t"" ""="" ""n""o""d""e""s""[""7""]""
"" "" "" "" ""n""o""d""e""s""[""7""]"".""l""e""f""t"" ""="" ""n""o""d""e""s""[""5""]""
"" "" "" "" ""n""o""d""e""s""[""7""]"".""r""i""g""h""t"" ""="" ""n""o""d""e""s""[""6""]""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""l""o""w""e""s""t""C""o""m""m""o""n""A""n""c""e""s""t""o""r""(""n""o""d""e""s""[""4""]"","" ""n""o""d""e""s""[""3""]"","" ""n""o""d""e""s""[""5""]"")""
