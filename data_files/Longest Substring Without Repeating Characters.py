
__author__ = 'Daniel'


class Solution:
    def lengthOfLongestSubstring(self, s):
        b = 0
        e = 0
        n = len(s)
        maxa = 0
        st = set()  
        while e < n:
            while s[e] in st:
                st.remove(s[b])
                b += 1

            st.add(s[e])
            e += 1
            maxa = max(maxa, e-b)

        return maxa

if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""e""n""g""t""h""O""f""L""o""n""g""e""s""t""S""u""b""s""t""r""i""n""g""(