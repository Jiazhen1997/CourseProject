
__author__ = 'Danyang'


class Solution(object):
    def __init__(self):
        import math

        MAX_MULT = int(math.log(10 ** 16) / math.log(5)) + 1
        self.M = [(i, (5 ** i - 1) / 4) for i in reversed(xrange(1, MAX_MULT + 1))]

    def solve_TLE(self, cipher):
        
        cnt = 0
        m = 0
        while True:
            if cnt >= cipher:
                break
            else:
                m2 = m
                while m2 != 0 and m2 % 5 == 0:
                    cnt += 1
                    m2 /= 5
                m += 5

        m -= 5
        return m

    def solve_math(self, cipher):
        
        n = cipher
        m = 0
        for i, p in self.M:
            if p <= n:
                cnt = n / p
                n -= cnt * p
                m += cnt * 5 ** i
        return m

    def solve(self, n):
        
        l = 0
        h = 5 * n
        while l <= h:
            mid = (l + h) / 2
            cnt = self.prime_count(5, mid)
            if cnt < n:
                l = mid + 1
            else:
                h = mid - 1
        return l

    def prime_count(self, p, n):
        
        if n < p:
            return 0

        return n / p + self.prime_count(p, n / p)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(