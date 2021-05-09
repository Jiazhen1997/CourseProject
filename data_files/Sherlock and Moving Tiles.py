

import math

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        L, S1, S2, qs = cipher
        v = abs(S1 - S2) / math.sqrt(2)
        rets = []
        for q in qs:
            t = (L - math.sqrt(q)) / v
            rets.append(t)
        return "\"n"".""j""o""i""n""(""m""a""p""(""l""a""m""b""d""a"" ""x"":"" 