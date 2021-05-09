
__author__ = 'Daniel'


class Solution:
    def longestPalindrome(self, s):
        
        n = len(s)
        pa = [[False for _ in xrange(n+1)] for _ in xrange(n)]
        for i in xrange(n):
            pa[i][i] = True
            pa[i][i+1] = True

        maxa = (0, 1)
        for i in xrange(n-2, -1, -1):
            for j in xrange(i+2, n+1):
                pa[i][j] = pa[i+1][j-1] and s[i] == s[j-1]
                if pa[i][j] and j-i > maxa[1]-maxa[0]:
                    maxa = (i, j)

        return s[maxa[0]:maxa[1]]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""o""n""g""e""s""t""P""a""l""i""n""d""r""o""m""e""(