
__author__ = 'Daniel'


class Solution(object):
    def isSubsequence(self, s, t):
        
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if t[j] != s[i]:
                j += 1
            else:
                i += 1
                j += 1

        return i == len(s)
