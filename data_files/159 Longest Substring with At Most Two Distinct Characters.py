
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        
        m = defaultdict(int)
        i = 0
        j = 0
        maxa = 0
        for j in xrange(len(s)):
            m[s[j]] += 1
            while len(m) > 2:
                m[s[i]] -= 1
                if m[s[i]] == 0:
                    del m[s[i]]

                i += 1

            maxa = max(maxa, j-i+1)

        return maxa


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""e""n""g""t""h""O""f""L""o""n""g""e""s""t""S""u""b""s""t""r""i""n""g""T""w""o""D""i""s""t""i""n""c""t""(