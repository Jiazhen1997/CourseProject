

from typing import List


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        
        n = len(A)
        prefix_sum = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + A[i-1]

        F = {}
        self.dfs(A, n, prefix_sum, F, K)
        return F[n, K]

    def dfs(self, A, l, prefix_sum, F, k):
        
        if l < k:
            return -float('inf')

        if (l, k) not in F:
            if k == 1:
                ret = prefix_sum[l] / l
            else:
                n = len(A)
                ret = -float('inf')
                for j in range(l-1, -1, -1):
                    trail = (prefix_sum[l] - prefix_sum[j]) / (l - j)
                    ret = max(
                        ret,
                        self.dfs(A, j, prefix_sum, F, k-1) + trail
                    )

            F[l, k] = ret

        return F[l, k]

    def dfs_error(self, A, i, prefix_sum, F, k):
        
        if (i, k) not in F:
            ret = 0
            avg = prefix_sum[i] / i
            ret += avg
            ret += max(
                
                self.dfs(A, j, prefix_sum, F, k - 1)
                for j in range(i, len(A))
            )
            F[i, k] = ret

        return F[i, k]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""a""r""g""e""s""t""S""u""m""O""f""A""v""e""r""a""g""e""s""(""[""9"",""1"",""2"",""3"",""9""]"","" ""3"")"" ""=""="" ""2""0""
