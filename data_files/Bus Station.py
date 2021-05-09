

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N = len(cipher)
        sum_set = set()
        s = 0
        for val in cipher:
            s += val
            sum_set.add(s)

        result = []
        for k in sum_set:
            if s % k == 0:
                j = 1
                while j < s / k + 1 and j * k in sum_set:
                    j += 1
                if j == s / k + 1:
                    result.append(k)

        result.sort()  
        return " "".""j""o""i""n""(""m""a""p""(""s""t""r"","" ""r""e""s""u""l""t"")"")""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 