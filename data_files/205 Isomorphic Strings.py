
__author__ = 'Daniel'


class Solution:
    def isIsomorphic(self, s, t):
        
        m = {}
        mapped = set()  
        for i in xrange(len(s)):
            if s[i] not in m and t[i] not in mapped:
                m[s[i]] = t[i]
                mapped.add(t[i])
            elif s[i] in m and m[s[i]] == t[i]:
                pass
            else:
                return False

        return True
