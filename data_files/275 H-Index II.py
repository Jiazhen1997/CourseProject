
__author__ = 'Daniel'


class Solution(object):
    def hIndex(self, A):
        
        n = len(A)
        s = 0
        e = n
        while s < e:
            m = (s+e)/2
            if A[m] >= n-m:
                e = m
            else:
                s = m+1

        return n-s


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""h""I""n""d""e""x""(""[""0"","" ""1"","" ""3"","" ""5"","" ""6""]"")"" ""=""="" ""3