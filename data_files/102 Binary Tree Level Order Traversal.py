
__author__ = 'Danyang'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        
        result = []
        q = []
        if root:
            q.append(root)

        while q:
            length = len(q)
            
            for i in range(length):
                cur = q[i]
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            result.append(map(lambda x: x.val, q[:length]))  
            q = q[length:]  
        return result

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""n""o""d""e""s"" ""="" ""[""T""r""e""e""N""o""d""e""(""i"")"" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""g""e""(""3"")""]""
"" "" "" "" ""n""o""d""e""s""[""0""]"".""l""e""f""t"" ""="" ""n""o""d""e""s""[""1""]""
"" "" "" "" ""n""o""d""e""s""[""1""]"".""l""e""f""t"" ""="" ""n""o""d""e""s""[""2""]""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""l""e""v""e""l""O""r""d""e""r""(""n""o""d""e""s""[""0""]"")""
""
""
