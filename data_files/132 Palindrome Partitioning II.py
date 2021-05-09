
__author__ = 'Danyang'


class Solution(object):
    def minCut(self, s):
        
        n = len(s)

        P = [[False for _ in xrange(n+1)] for _ in xrange(n+1)]
        for i in xrange(n+1):  
            P[i][i] = True
        for i in xrange(n):  
            P[i][i+1] = True

        for i in xrange(n, -1, -1):  
            for j in xrange(i+2, n+1):
                P[i][j] = P[i+1][j-1] and s[i] == s[j-1]

        C = [i for i in xrange(n+1)]  
        for i in xrange(n+1):
            if P[0][i]:
                C[i] = 0
            else:
                C[i] = min(
                    C[j] + 1
                    for j in xrange(i)
                    if P[j][i]
                )

        return C[n]

    def minCut_dp(self, s):
        
        if not s:
            return 0

        length = len(s)
        
        P = [[False for _ in xrange(length+1)] for _ in xrange(length+1)]
        for i in xrange(length+1):
            try:
                P[i][i] = True
                P[i][i+1] = True
            except IndexError:
                pass

        for i in xrange(length, -1, -1):
            for j in xrange(i+2, length+1):
                try:
                    P[i][j] = P[i+1][j-1] and s[i] == s[j-1]
                except IndexError:
                    P[i][j] = True

        
        D = [length-i-1 for i in xrange(length)]  
        for i in xrange(length-1, -1, -1):
            if P[i][length]:
                D[i] = 0
            else:
                for j in xrange(i+1, length):
                    if P[i][j]:
                        D[i] = min(D[i], D[j]+1)
        return D[0]

    def minCut_MLE(self, s):
        
        q = [[s]]
        count = -1
        while q:
            
            length = len(q)
            count += 1
            for cur_level in xrange(length):
                cur = q[cur_level]
                if all(self.is_palindrome(item) for item in cur):
                    return count
                
                for ind, val in enumerate(cur):
                    for i in xrange(1, len(val)):
                        cut1 = val[:i]
                        cut2 = val[i:]
                        new_cur = list(cur)
                        new_cur[ind] = cut1
                        new_cur.insert(ind+1, cut2)
                        q.append(new_cur)
            q = q[length:]

    def minCut_TLE(self, s):
        
        if not s:
            return 0

        length = len(s)
        dp = [[1<<32-1 for _ in xrange(length+1)] for _ in xrange(length+1)]
        for i in xrange(length+1):
            try:
                dp[i][i] = 0
                dp[i][i+1] = 0
            except IndexError:
                pass

        for i in xrange(length, -1, -1):
            for k in xrange(i, length+1):
                if self.is_palindrome(s[i:k]):
                    dp[i][k] = 0
                else:
                    dp[i][k] = min(1+dp[i][j]+dp[j][k] for j in xrange(i+1, k))

        return dp[0][length]

    def is_palindrome(self, s):
        return s == s[::-1]

    def minCut_TLE2(self, s):
        
        if not s:
            return 0

        length = len(s)
        
        dp2 = [[False for _ in xrange(length+1)] for _ in xrange(length+1)]
        for i in xrange(length+1):
            try:
                dp2[i][i] = True
                dp2[i][i+1] = True
            except IndexError:
                pass

        for i in xrange(length, -1, -1):
            for j in xrange(i+2, length+1):
                try:
                    dp2[i][j] = dp2[i+1][j-1] and s[i] == s[j-1]
                except IndexError:
                    dp2[i][j] = True


        
        dp = [[1<<32-1 for _ in xrange(length+1)] for _ in xrange(length+1)]
        for i in xrange(length+1):
            try:
                dp[i][i] = 0
                dp[i][i+1] = 0
            except IndexError:
                pass

        for i in xrange(length, -1, -1):
            for k in xrange(i, length+1):
                if dp2[i][k]:
                    dp[i][k] = 0
                else:
                    dp[i][k] = min(1+dp[i][j]+dp[j][k] for j in xrange(i+1, k))

        return dp[0][length]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""i""n""C""u""t""(