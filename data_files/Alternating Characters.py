

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        lst = list(cipher)
        ret = [lst[0]]
        cnt = 0
        for i in xrange(1, len(lst)):
            if lst[i] != ret[-1]:
                ret.append(lst[i])
            else:
                cnt += 1
        return cnt


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(