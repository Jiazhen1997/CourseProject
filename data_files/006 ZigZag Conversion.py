
__author__ = 'Danyang'


class Solution:
    def convert(self, s, nRows):
        
        length = len(s)
        matrix = [[] for _ in xrange(nRows)]

        i = 0
        while i < length:
            try:
                
                for j in xrange(nRows):
                    matrix[j].append(s[i])
                    i += 1

                
                for j in xrange(nRows-1-1, 0, -1):
                    matrix[j].append(s[i])
                    i += 1

            except IndexError:
                break

        lst = ["".""j""o""i""n""(""e""l""e""m""e""n""t"")"" ""f""o""r"" ""e""l""e""m""e""n""t"" ""i""n"" ""m""a""t""r""i""x""]""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 