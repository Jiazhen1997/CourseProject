
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        S, p, q = cipher
        n = len(p)
        S = int(S)
        global_max = 0
        for i in xrange(n):  
            global_max = max(global_max, self.get_longest(S, p, q, i, 0), self.get_longest(S, p, q, 0, i))

        return global_max

    def get_longest(self, S, p, q, i, j):
        start_i = i
        start_j = j
        local_max = 0
        n = len(p)
        cur_diff = 0
        while i < n and j < n:
            if p[i] != q[j]:
                cur_diff += 1

            if cur_diff > S:  
                while p[start_i] == q[start_j]:
                    start_i += 1
                    start_j += 1
                start_i += 1
                start_j += 1
                cur_diff -= 1

            local_max = max(local_max, i - start_i + 1)

            i += 1
            j += 1

        return local_max


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(