

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        l = 1
        h = cipher
        while l <= h:
            mid = (l + h) / 2
            if self.sum_of_squares(mid) <= cipher:
                l = mid + 1
            else:
                h = mid - 1

        l -= 1
        return l

    def sum_of_squares(self, n):
        return n * (n + 1) * (2 * n + 1) / 6


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(