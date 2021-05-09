
__author__ = 'Daniel'


class Solution:
    def combinationSum3(self, k, n):
        
        ret = []
        self.dfs(k, n, [], ret)
        return ret

    def dfs(self, remain_k, remain_n, cur, ret):
        if remain_k == 0 and remain_n == 0:
            ret.append(list(cur))
            return

        
        if remain_k * 9 < remain_n or remain_k * 1 > remain_n:
            return

        start = 1
        if cur:
            start = cur[-1] + 1  
        for i in xrange(start, 10):
            cur.append(i)
            self.dfs(remain_k - 1, remain_n - i, cur, ret)
            cur.pop()


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""o""m""b""i""n""a""t""i""o""n""S""u""m""3""(""3"","" ""9"")"" ""=""="" ""[""[""1"","" ""2"","" ""6""]"","" ""[""1"","" ""3"","" ""5""]"","" ""[""2"","" ""3"","" ""4""]""]""
