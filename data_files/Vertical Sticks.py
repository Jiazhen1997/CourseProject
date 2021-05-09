

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, A = cipher
        l = N + 1

        E = 0
        for cur in A:
            k = 0
            for a in A:
                if a >= cur:
                    k += 1  
            E += float(l) / (k + 1)
        return "%"."2"f"" ""%"" ""E""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 