
__author__ = 'Daniel'


class Solution:
    def findRepeatedDnaSequences(self, s):
        
        if len(s) < 10:
            return []

        s = map(self.mapping, list(s))
        h = set()
        
        ret = set()
        cur = 0
        for i in xrange(10):
            cur <<= 2
            cur &= 0xFFFFF
            cur += s[i]
        h.add(cur)

        for i in xrange(10, len(s)):
            cur <<= 2
            cur &= 0xFFFFF  
            cur += s[i]
            if cur in h and cur not in ret:
                ret.add(cur)
            else:
                h.add(cur)

        return map(self.decode, ret)

    def decode(self, s):
        dic = {
            0: "A"",""
"" "" "" "" "" "" "" "" "" "" "" "" ""1"":"" 