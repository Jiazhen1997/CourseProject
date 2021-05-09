
__author__ = 'Danyang'


class Solution:
    def maxKSubArrays(self, nums, k):
        
        n = len(nums)
        f = [[0 for _ in xrange(k+1)] for _ in xrange(n+1)]
        g = [[0 for _ in xrange(k+1)] for _ in xrange(n+1)]

        s = [0 for _ in xrange(n+1)]  
        for i in xrange(1, n+1):
            s[i] = s[i-1]+nums[i-1]

        for i in xrange(1, n+1):
            for st in xrange(1, k+1):
                if st == 1:  
                    f[i][st] = max([s[i]-s[j] for j in xrange(i)])
                else:
                    f[i][st] = max([g[j][st-1]+s[i]-s[j] for j in xrange(i)])

                g[i][st] = max([f[j][st] for j in xrange(i+1)])

        maxa = -1<<31
        for i in xrange(1, n+1):
            maxa = max(maxa, g[i][k])
        return maxa


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""K""S""u""b""A""r""r""a""y""s""(""[""1"","" ""2"","" ""3""]"","" ""1"")""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""K""S""u""b""A""r""r""a""y""s""(""[""-""1"","" ""-""2"","" ""-""3"","" ""-""1""0""0"","" ""-""1"","" ""-""5""0""]"","" ""2"")