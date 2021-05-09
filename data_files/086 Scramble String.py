
__author__ = 'Danyang'
class Solution:
    def isScramble(self, s1, s2):
        
        if len(s1)!=len(s2):
            return False
        chars = [0 for _ in xrange(26)]
        for char in s1:
            chars[ord(char)-ord('a')] += 1
        for char in s2:
            chars[ord(char)-ord('a')] -= 1

        
        
        for val in chars:
            if val!=0:
                return False

        if len(s1)==1:
            return True


        for i in xrange(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or \
                self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:len(s2)-i]):
                return True

        return False



if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""i""s""S""c""r""a""m""b""l""e""(