



class Solution:
    def findContentChildren(self, g, s):
        
        g.sort()
        s.sort()
        ret = 0
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                ret += 1
                i += 1
                j += 1
            else:
                j += 1

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""C""o""n""t""e""n""t""C""h""i""l""d""r""e""n""(""[""1""0"",""9"",""8"",""7""]"","" ""[""5"",""6"",""7"",""8""]"")"" ""=""="" ""2""
