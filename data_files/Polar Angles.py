
import math

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        cipher.sort(cmp=self.cmp)


    def cmp_polar(self, a, b):
        
        x1 = a[0]
        y1 = a[1]
        x2 = b[0]
        y2 = b[1]
        
        cross_product = x1 * y2 - x2 * y1
        if cross_product > 0:
            return -1
        elif cross_product < 0:
            return 1
        else:
            if x1 * x1 >= 0 and y1 * y1 >= 0:
                return x1 * x1 + y1 * y1 - x2 * x2 - y2 * y2
            else:
                if y1 > 0:
                    return -1
                if y2 > 0:
                    return 1
                if y1 == 0 and x1 > 0:
                    return -1
                else:
                    return 1

    def cmp(self, a, b):
        
        x1 = a[0]
        y1 = a[1]
        x2 = b[0]
        y2 = b[1]
        r1 = x1 * x1 + y1 * y1
        r2 = x2 * x2 + y2 * y2
        phi1 = math.atan2(y1, x1)
        phi2 = math.atan2(y2, x2)
        if phi1 < 0:
            phi1 += math.pi * 2
        if phi2 < 0:
            phi2 += math.pi * 2
        if phi1 < phi2:
            return -1
        elif phi1 > phi2:
            return 1
        else:
            return r1 - r2


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(