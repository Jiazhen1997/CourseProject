
__author__ = 'Danyang'


class Solution(object):
    def __init__(self):
        self.combs = {}

    def solve(self, cipher):
        
        C, N = cipher
        return self.get_combinations(N, C, 0)

    
    def get_combinations(self, t, lst, k):
        if t == 0:
            return 1

        if t < 0 or k >= len(lst):
            return 0

        if (t, k) not in self.combs:
            cnt = 0
            while t >= 0:
                cnt += self.get_combinations(t, lst, k + 1)
                t -= lst[k]
            self.combs[(t, k)] = cnt

        return self.combs[(t, k)]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(