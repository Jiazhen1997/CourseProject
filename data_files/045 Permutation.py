
__author__ = 'Danyang'
class Solution:
    def permute(self, num):
        
        result = []
        self.get_permute(num, [], result)
        return result

    def get_permute(self, seq, current, result):
        length = len(seq)
        if length==0:
            result.append(current)

        for ind, val in enumerate(seq):
            
            self.get_permute(seq[:ind]+seq[ind+1:], current+[val], result)  
            
            
            

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""p""e""r""m""u""t""e""(""[""1"","" ""2"","" ""3""]"")