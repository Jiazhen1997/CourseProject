
__author__ = 'Danyang'


class Solution(object):
    def longestPalindrome(self, s):
        
        if not s:
            return
        n = len(s)
        if n == 1:
            return s

        ret = s[0]
        for i in xrange(0, n):
            cur = self.get_palindrome_from_center(s, i, i)  
            if len(cur) > len(ret): ret = cur
            cur = self.get_palindrome_from_center(s, i, i+1)
            if len(cur) > len(ret): ret = cur
        return ret

    def longestPalindrome_TLE(self, s):
        
        length = len(s)
        dp = [[False for _ in xrange(length+1)] for _ in xrange(length+1)]
        for i in xrange(length+1):
            dp[i][i] = True

        longest = [0, 0]
        for j in xrange(length+1):
            for i in xrange(j-1, -1, -1):
                if i+1 == j:
                    dp[i][j] = True
                else:
                    dp[i][j] = s[i] == s[j-1] and dp[i+1][j-1]  

                if dp[i][j] == True and longest[1]-longest[0] < j-i:
                    longest[0], longest[1] = i, j

        return s[longest[0]:longest[1]]

    def longestPalindrome_TLE2(self, s):
        
        length = len(s)

        longest = ""
"" "" "" "" "" "" "" "" ""d""p"" ""="" ""[""[""F""a""l""s""e"" ""f""o""r"" ""_"" ""i""n"" ""x""r""a""n""g""e""(""l""e""n""g""t""h""+""1"")""]"" ""f""o""r"" ""_"" ""i""n"" ""x""r""a""n""g""e""(""l""e""n""g""t""h""+""1"")""]"" "" ""#"" ""l""a""r""g""e""r"" ""t""h""a""n"" ""u""s""u""a""l""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""l""e""n""g""t""h""+""1"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""d""p""[""i""]""[""i""]"" ""="" ""T""r""u""e"" "" ""#"" ""e""m""p""t""y""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""l""e""n""g""t""h"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""d""p""[""i""]""[""i""+""1""]"" ""="" ""T""r""u""e"" "" ""#"" ""s""i""n""g""l""e"" ""c""h""a""r""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""l""e""n""g""t""h""-""1"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""d""p""[""i""]""[""i""+""2""]"" ""="" ""s""[""i""]"" ""=""="" ""s""[""i""+""1""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""d""p""[""i""]""[""i""+""1""]"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""l""o""n""g""e""s""t"" ""="" ""s""[""i"":""i""+""2""]""
""
"" "" "" "" "" "" "" "" ""f""o""r"" ""l"" ""i""n"" ""x""r""a""n""g""e""(""3"","" ""l""e""n""g""t""h""+""1"")"":"" "" ""#"" ""b""r""e""a""d""t""h""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""0"","" ""l""e""n""g""t""h""-""l"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""s""[""i""]"" ""=""="" ""s""[""i""+""l""-""1""]"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""d""p""[""i""]""[""i""+""l""]"" ""="" ""d""p""[""i""+""1""]""[""i""+""l""-""1""]""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""d""p""[""i""]""[""i""+""l""]"" ""="" ""F""a""l""s""e""
""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""d""p""[""i""]""[""i""+""l""]"" ""a""n""d"" ""l""e""n""(""l""o""n""g""e""s""t"")"" ""<"" ""l"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""l""o""n""g""e""s""t"" ""="" ""s""[""i"":""i""+""l""]""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""l""o""n""g""e""s""t""
""
"" "" "" "" ""d""e""f"" ""g""e""t""_""p""a""l""i""n""d""r""o""m""e""_""f""r""o""m""_""c""e""n""t""e""r""(""s""e""l""f"","" ""s"","" ""b""e""g""i""n"","" ""e""n""d"")"":""
"" "" "" "" "" "" "" "" 
        while begin >= 0 and end < len(s) and s[begin] == s[end]:
            begin -= 1
            end += 1

        return s[begin+1: end-1+1]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""o""n""g""e""s""t""P""a""l""i""n""d""r""o""m""e""(