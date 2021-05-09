
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, v = cipher
        v.reverse()  
        
        s = [0 for _ in xrange(N + 1)]
        for i in xrange(1, N + 1):
            s[i] = s[i - 1] + v[i - 1]

        f = [[0, 0] for _ in xrange(N + 1)]
        for i in xrange(1, N + 1):
            
            local_max = 0
            for k in xrange(1, 4):
                if i - k >= 0:
                    local_max = max(local_max, s[i] - s[i - k] + s[i - k] - f[i - k][1])
            f[i][0] = local_max

            
            
            local_max = 0
            for k in xrange(1, 4):
                if i - k >= 0:
                    local_max = max(local_max, s[i] - s[i - k] + s[i - k] - f[i - k][0])
            f[i][1] = local_max

        return f[-1][0]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(