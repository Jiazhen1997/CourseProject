
__author__ = 'Danyang'
class Solution:
    def partition(self, s):
        
        result = []
        self.get_partition(s, [], result)
        return result

    def get_partition(self, seq, cur, result):
        if not seq:
            result.append(cur)

        
        for i in xrange(len(seq)):
            if self.is_palindrome(seq[:i+1]):  
                self.get_partition(seq[i+1:], cur+[seq[:i+1]], result)


    def is_palindrome(self, s):
        
        
        return s == s[::-1]

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""p""a""r""t""i""t""i""o""n""(