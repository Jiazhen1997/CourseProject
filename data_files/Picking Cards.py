
__author__ = 'Danyang'
MOD = 1000000007


class Solution(object):
    def solve(self, cipher):
        
        N, A = cipher
        cnts = [0 for _ in xrange(N + 1)]
        for num in A:
            cnts[num] += 1

        if 0 not in cnts:
            return 0

        
        result = 1
        paths = cnts[0]
        for i in xrange(1, N):
            if paths <= 0:
                return 0
            result *= paths  
            result %= MOD
            paths += cnts[i]
            paths -= 1  

        return result


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(