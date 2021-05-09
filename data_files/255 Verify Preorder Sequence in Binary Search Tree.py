
__author__ = 'Daniel'


class Solution:
    def verifyPreorder(self, preorder):
        
        left_finished = None
        stk = []
        for num in preorder:
            if left_finished and num < left_finished:
                return False

            while stk and stk[-1] < num:
                left_finished = stk.pop()

            stk.append(num)

        return True


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""e""o""r""d""e""r"" ""="" ""[""3"","" ""5"","" ""2"","" ""1"","" ""4"","" ""7"","" ""6"","" ""9"","" ""8"","" ""1""0""]""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""v""e""r""i""f""y""P""r""e""o""r""d""e""r""(""p""r""e""o""r""d""e""r"")"" ""=""="" ""F""a""l""s""e""
