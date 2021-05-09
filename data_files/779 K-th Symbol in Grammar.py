



class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        
        return self.dfs(N, K, True)

    def dfs(self, N, K, not_flip):
        if N == 1:
            return 0 if not_flip else 1
        half_l = 2 ** (N - 1) // 2
        if K <= half_l:
            return self.dfs(N - 1, K, not_flip)
        else:
            return self.dfs(N - 1, K - half_l, not not_flip)

    def kthGrammar_TLE(self, N: int, K: int) -> int:
        
        row = 0
        pos = 1
        for n in range(1, N):
            row = (row << pos) + (~row & 2 ** pos - 1)
            pos *= 2

        ret = row >> pos - K & 1
        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""k""t""h""G""r""a""m""m""a""r""(""1"","" ""1"")"" ""=""="" ""0""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""k""t""h""G""r""a""m""m""a""r""(""2"","" ""1"")"" ""=""="" ""0""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""k""t""h""G""r""a""m""m""a""r""(""2"","" ""2"")"" ""=""="" ""1""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""k""t""h""G""r""a""m""m""a""r""(""4"","" ""5"")"" ""=""="" ""1""
