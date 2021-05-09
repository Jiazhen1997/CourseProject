
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, K, lst = cipher

        hm = {}
        for val in lst:
            if val in hm:
                hm[val] += 1
            else:
                hm[val] = 1

        cnt = 0
        for val in lst:
            target = val + K
            if target in hm:
                cnt += hm[target]
        return cnt


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(