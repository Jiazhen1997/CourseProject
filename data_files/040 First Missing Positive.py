
__author__ = 'Danyang'
class Solution:
    def firstMissingPositive(self, A):
        
        if not A:
            return 1

        i = 0
        length = len(A)
        while i<length:
            current = A[i]
            if current<=0 or current>length or A[current-1]==current:  
                i += 1
            else:
                A[current-1], A[i] = current, A[current-1]   


        for i in xrange(length):
            if A[i]!=i+1:
                return i+1
        return A[-1]+1


if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""r""s""t""M""i""s""s""i""n""g""P""o""s""i""t""i""v""e""(""[""3"",""4"",""-""1"",""1""]"")""=""=""2