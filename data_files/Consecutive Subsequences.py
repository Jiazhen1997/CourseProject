
__author__ = 'Danyang'


class Solution_TLE(object):
    def solve(self, cipher):
        
        n, k, a = cipher
        f = [0 for _ in xrange(n + 1)]  
        for i in xrange(1, n + 1):
            f[i] = f[i - 1] + a[i - 1]

        result = 0
        for i in xrange(1, n + 1):
            for j in xrange(0, i):
                if (f[i] - f[j]) % k == 0:
                    result += 1
        return result


class Solution(object):
    def solve(self, cipher):
        
        n, k, a = cipher
        cnts = [0 for _ in xrange(k)]

        s = 0
        cnts[0] = 1  
        for num in a:
            s += num
            s %= k
            cnts[s] += 1

        result = 0
        for cnt in cnts:
            result += (cnt * (cnt - 1)) / 2  
        return result


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(