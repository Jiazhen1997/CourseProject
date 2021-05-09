
__author__ = 'Danyang'


class Solution(object):
    def solve_TLE(self, cipher):
        
        N, K, lst = cipher
        lst.sort()
        global_min = 1 << 32 - 1
        for i in xrange(N - K):
            seq = lst[i: i + K]
            global_min = min(global_min, max(seq) - min(seq))

        return global_min

    def solve_TLE2(self, cipher):
        
        N, K, lst = cipher
        lst.sort()

        seq = lst[0: K]
        mini = min(seq)
        maxa = max(seq)
        global_min = maxa - mini
        for i in xrange(K, N):
            popped = seq.pop(0)
            cur = lst[i]
            seq.append(cur)
            if popped != mini:
                mini = min(mini, cur)
            else:
                mini = min(seq)
            if popped != maxa:
                maxa = max(maxa, cur)
            else:
                maxa = max(seq)

            global_min = min(global_min, maxa - mini)

        return global_min


    def solve(self, cipher):
        
        N, K, lst = cipher
        lst.sort()

        mini = lst[0]
        maxa = lst[K - 1]
        global_min = maxa - mini
        for i in xrange(1, N - K):
            mini = lst[i]
            maxa = lst[i + K - 1]
            global_min = min(global_min, maxa - mini)

        return global_min


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(