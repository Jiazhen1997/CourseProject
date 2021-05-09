
import math

__author__ = 'Daniel'


class Solution:
    def countPrimes(self, n):
        
        if n < 3:
            return 0

        is_prime = [True for _ in xrange(n)]
        is_prime[0], is_prime[1] = False, False
        for i in xrange(2, int(math.sqrt(n))+1):
            if is_prime[i]:
                for j in xrange(i*i, n, i):
                    is_prime[j] = False

        return is_prime.count(True)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""o""u""n""t""P""r""i""m""e""s""(""1""5""0""0""0""0""0"")"" ""=""="" ""1""1""4""1""5""5