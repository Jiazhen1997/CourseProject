
__author__ = 'Danyang'


class Solution(object):
    def kSumII(self, A, k, target):
        
        ret = []
        self.dfs(A, 0, k, [], target, ret)
        return ret

    def dfs(self, A, i, k, cur, remain, ret):
        
        if len(cur) == k and remain == 0:
            ret.append(list(cur))
            return

        if i >= len(A) or len(cur) > k or len(A)-i+len(cur) < k:
            return

        self.dfs(A, i+1, k, cur, remain, ret)
        cur.append(A[i])
        self.dfs(A, i+1, k, cur, remain-A[i], ret)
        cur.pop()

    def dfs_array(self, A, k, cur, remain, ret):
        
        if len(cur) == k and remain == 0:
            ret.append(list(cur))

        if not A or len(cur) >= k or len(A)+len(cur) < k:
            return

        
        num = A.pop(0)  

        self.dfs_array(A, k, cur, remain, ret)
        cur.append(num)
        self.dfs_array(A, k, cur, remain-num, ret)
        cur.pop()

        A.push(0, num)

    def dfs_stk(self, A, k, cur, remain, ret):
        
        if len(cur) == k and remain == 0:
            ret.append(list(cur))

        if not A or len(cur) >= k or len(A)+len(cur) < k:
            return

        
        num = A.pop()

        self.dfs(A, k, cur, remain, ret)
        cur.append(num)
        self.dfs(A, k, cur, remain-num, ret)
        cur.pop()

        A.append(num)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""k""S""u""m""I""I""(""[""1"","" ""2"","" ""3"","" ""4""]"","" ""2"","" ""5"")""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""k""S""u""m""I""I""(""[""1"","" ""2"","" ""3"","" ""4""]"","" ""2"","" ""5"")"" ""=""="" ""[""[""3"","" ""2""]"","" ""[""1"","" ""4""]""]