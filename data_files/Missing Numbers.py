
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        m, A, n, B = cipher

        result = set()  
        hm = {}
        for a in A:
            if a not in hm:
                hm[a] = 1
            else:
                hm[a] += 1

        for b in B:
            if b not in hm or hm[b] <= 0:
                result.add(b)
            else:
                hm[b] -= 1
        result = sorted(list(result))
        return " "".""j""o""i""n""(""m""a""p""(""s""t""r"","" ""r""e""s""u""l""t"")"")""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 