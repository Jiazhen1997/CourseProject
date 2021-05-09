
__author__ = 'Danyang'
class Solution:
    def climbStairs_save_memory(self, n):
        
        f_n_minus_2 = 1  
        f_n_minus_1 = 2  
        if n==1: return f_n_minus_2
        if n==2: return f_n_minus_1
        fn = 0
        for i in range(2, n):
            fn = f_n_minus_1 +f_n_minus_2
            
            f_n_minus_2 = f_n_minus_1
            f_n_minus_1 = fn
        return fn

    def climbStairs(self, n):
        
        if n==1: return 1
        if n==2: return 2
        f = [0 for _ in xrange(n+1)]
        f[0] = 0
        f[1] = 1
        f[2] = 2
        for i in xrange(3, n+1):
            f[i] = f[i-1]+f[i-2]
        return f[n]


if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""c""l""i""m""b""S""t""a""i""r""s""(""3"")