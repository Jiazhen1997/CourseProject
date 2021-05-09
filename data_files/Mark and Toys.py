

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        n, K, A = cipher
        A.sort()
        cnt = 0
        for elt in A:
            K -= elt
            if K >= 0:
                cnt += 1
            else:
                break
        return cnt


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(