
__author__ = 'Danyang'
class Solution:
    def grayCode(self, n):
        
        if n==0:
            return [0]
        result = [0, 1]

        for num_of_bit in range(2, n+1):
            msb = 1<<num_of_bit-1
            for element in reversed(result):
                result.append(msb+element)

        return result


    def grayCode_math(self, n):
        
        return [(x>>1)^x for x in xrange(1<<n)]
