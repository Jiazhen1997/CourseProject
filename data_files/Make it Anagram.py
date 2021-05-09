
__author__ = 'Danyang'


class Solution(object):
    def solve_MLE(self, cipher):
        
        a, b = cipher
        a, b = list(a), list(b)
        m = len(a)
        n = len(b)
        a.sort()
        b.sort()

        dp = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        for i in xrange(m + 1):
            dp[i][0] = i
        for j in xrange(n + 1):
            dp[0][j] = j
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[-1][-1]

    def solve(self, cipher):
        
        a, b = cipher
        bucket = [0 for _ in xrange(26)]
        for char in a:
            bucket[ord(char) - ord('a')] += 1
        for char in b:
            bucket[ord(char) - ord('a')] -= 1

        counter = 0
        for ind, val in enumerate(bucket):
            counter += abs(val - 0)

        return counter


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(