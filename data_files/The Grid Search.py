
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        matrix, pattern = cipher

        R1, C1 = len(matrix), len(matrix[0])
        R2, C2 = len(pattern), len(pattern[0])

        dp = [[0 for _ in xrange(C1 + 1)] for _ in xrange(R1 + 1)]  

        for i in xrange(1, R1 + 1):
            for j in xrange(1, C1 + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + matrix[i - 1][j - 1]

        pattern_sum = sum([sum(pattern[i]) for i in xrange(R2)])

        for i in xrange(R1 - R2 + 1):
            for j in xrange(C1 - C2 + 1):
                
                
                bottom = i + R2
                left = j + C2
                candidate_sum = dp[bottom][left] - dp[bottom][j] - dp[i][left] + dp[i][j]

                if candidate_sum == pattern_sum:
                    matched = True
                    for a in xrange(R2):
                        for b in xrange(C2):
                            if matrix[i + a][j + b] != pattern[a][b]:
                                matched = False
                                break
                        if not matched:
                            break
                    if matched:
                        return "Y"E"S""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 