

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, K, lst = cipher
        for i in xrange(len(lst)):
            if K <= 0:
                break
            maxa, idx = -1, 0
            for j in xrange(i, len(lst)):
                if lst[j] > maxa:
                    maxa = lst[j]
                    idx = j
            if idx != i:
                K -= 1
                lst[idx], lst[i] = lst[i], lst[idx]

        return " "".""j""o""i""n""(""m""a""p""(""s""t""r"","" ""l""s""t"")"")""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 