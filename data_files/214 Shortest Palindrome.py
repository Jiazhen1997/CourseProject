
__author__ = 'Daniel'


class Solution:
    def shortestPalindrome(self, s):
        
        s_r = s[::-1]
        l = len(s)
        if l < 2:
            return s

        
        T = [0 for _ in xrange(l+1)]
        T[0] = -1
        pos = 2
        cnd = 0
        while pos <= l:
            if s[pos-1] == s[cnd]:
                T[pos] = cnd+1
                cnd += 1
                pos += 1
            elif T[cnd] != -1:
                cnd = T[cnd]
            else:
                T[pos] = 0
                cnd = 0
                pos += 1

        
        i = 0
        b = 0
        while i+b < l:
            if s[i] == s_r[i+b]:
                i += 1
                if i == l:
                    return s
            elif T[i] != -1:
                b = b+i-T[i]
                i = T[i]
            else:
                b += 1
                i = 0

        
        return s_r+s[i:]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""s""h""o""r""t""e""s""t""P""a""l""i""n""d""r""o""m""e""(