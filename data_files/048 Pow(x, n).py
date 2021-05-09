
__author__ = 'Danyang'


class Solution:
    def pow(self, x, n):
        
        invert_flag = False if n > 0 else True
        
        n = abs(n)
        product = 1.0
        while n > 0:
            if n & 1 == 1:
                product *= x

            n = n >> 1
            x *= x

        if invert_flag:
            product = 1.0 / product

        return product

    
    
    
    def pow_TLE(self, x, n):
        
        if abs(x)<=0.00001:
            return 0
        if x==1.0:
            return 1
        if x==-1.0:
            if n&1==1:
                return 1
            else:
                return -1

        if abs(x-1.0)<1e-6:
            return 1+(x-1.0)*n

        if abs(x--1.0)<1e-6:
            if n % 2==0:
                return self.pow(-x, n)
            else:
                return -self.pow(-x, n)

        product = 1.0
        for i in xrange(abs(n)):
            pre = product
            if n>0:
                product *= x
            else:
                product /= x

            if abs(product - pre)<1e-5:
                break

        return product


if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""p""o""w""(""8"".""8""8""0""2""3"","" ""3"")""
