
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        hm = {}
        cnt = 0
        for ind, val in enumerate(cipher):
            if val in hm:
                cnt += 2 * len(hm[val])
                hm[val].append(ind)
            else:
                hm[val] = [ind]
        return cnt


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(