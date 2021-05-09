

from collections import Counter


class Solution:
    def findMaxForm(self, strs, m, n):
        
        if not strs:
            return 0

        F = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        z, o = self.count(strs[0])
        for i in range(m+1):
            for j in range(n+1):
                if i + z<= m and j + o <= n:
                    F[i][j] = 1

        for e in range(1, len(strs)):
            z, o = self.count(strs[e])
            for i in range(m+1):
                for j in range(n+1):
                    if i + z <= m and j + o <= n:
                        F[i][j] = max(
                            F[i][j],
                            F[i + z][j + o] + 1
                        )

        ret = max(
            F[i][j]
            for i in range(m + 1)
            for j in range(n + 1)
        )
        return ret

    def count(self, s):
        z, o = 0, 0
        for e in s:
            if e == "0"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""z"" ""+""="" ""1""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""o"" ""+""="" ""1""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""z"","" ""o""
""
"" "" "" "" ""d""e""f"" ""f""i""n""d""M""a""x""F""o""r""m""_""T""L""E""(""s""e""l""f"","" ""s""t""r""s"","" ""m"","" ""n"")"":""
"" "" "" "" "" "" "" "" 
        if not strs:
            return 0

        F = [[[0 for _ in range(len(strs))] for _ in range(n + 1)] for _ in range(m + 1)]
        count = Counter(strs[0])
        for i in range(m+1):
            for j in range(n+1):
                if i + count["0""]"" ""<""="" ""m"" ""a""n""d"" ""j"" ""+"" ""c""o""u""n""t""[
        0-1 knapsack
        let F[p][q][i] be the max end at A[i], with p 0's and q 1's
        F[p][q][i] = max(F[p'][q'][i-1] + 1, F[p][q][i-1])

        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        
        reward is 1 regarless of length, then greedy - error

        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        