
__author__ = 'Daniel'


class Solution(object):
    def lengthLongestPath(self, input):
        
        input = input.split('\n')
        F = []
        gmax = 0
        for elt in input:
            idx = elt.count('\t')
            idx = min(idx, len(F))
            e = elt.strip('\t')
            prev = -1 if idx == 0 else F[idx-1]
            if idx == len(F):
                F.append(prev + 1 + len(e))
            else:
                F[idx] = prev + 1 + len(e)  

            if '.' in elt:
                gmax = max(gmax, F[idx])

        return gmax

if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""e""n""g""t""h""L""o""n""g""e""s""t""P""a""t""h""(