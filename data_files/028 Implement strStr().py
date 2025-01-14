
__author__ = 'Danyang'
class Solution:
    def strStr_brute_force(self, haystack, needle):
        
        l_hay = len(haystack)
        l_ndl = len(needle)
        for i in xrange(l_hay-l_ndl+1):  
            if haystack[i:i+l_ndl]==needle:
                return haystack[i:]
        return None

    def strStr(self, haystack, needle):
        
        ln = len(needle)
        lh = len(haystack)
        if ln==0:
            return haystack
        if ln==1:
            try:
                index = haystack.index(needle)
                return haystack[index:]
            except ValueError:
                return None

        
        T = [0 for _ in xrange(ln)]
        T[0] = -1
        T[1] = 0
        pos = 2
        cnd = 0
        while pos<ln:
            if needle[pos-1]==needle[cnd]:  
                cnd += 1
                T[pos] = cnd
                pos += 1
            elif T[cnd]!=-1:
                cnd = T[cnd]
            else:
                cnd = 0
                T[pos] = cnd
                pos += 1

        
        i = 0
        m = 0
        while m+i<lh:
            if needle[i]==haystack[m+i]:
                i += 1
                if i==ln:
                    return haystack[m:]
            else:
                if T[i]!=-1:
                    m = m+i-T[i]
                    i = T[i]
                else:
                    m += 1
                    i = 0

        return None


if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""n""e""e""d""l""e"" ""="" 