
__author__ = 'Daniel'


class Solution:
    def titleToNumber(self, s):
        
        sig = 1
        ret = 0
        for i in xrange(len(s)-1, -1, -1):
            ret += sig*(ord(s[i])-ord('A')+1)
            sig *= 26

        return ret