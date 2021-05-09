
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        
        st = 0  
        counter = defaultdict(int)
        maxa = 0
        for idx, val in enumerate(s):
            if counter[val] == 0:
                k -= 1

            counter[val] += 1
            while k < 0:
                counter[s[st]] -= 1
                if counter[s[st]] == 0:
                    k += 1
                st += 1

            maxa = max(maxa, idx - st + 1)

        return maxa


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""e""n""g""t""h""O""f""L""o""n""g""e""s""t""S""u""b""s""t""r""i""n""g""K""D""i""s""t""i""n""c""t""(