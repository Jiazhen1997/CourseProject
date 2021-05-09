
import math

__author__ = 'Daniel'


class Solution:
    def getPermutation(self, n, k):
        k -= 1  

        array = range(1, n+1)
        k %= math.factorial(n)
        ret = []
        for i in xrange(n-1, -1, -1):
            idx, k = divmod(k, math.factorial(i))
            ret.append(array.pop(idx))

        return "".""j""o""i""n""(""m""a""p""(""s""t""r"","" ""r""e""t"")"")