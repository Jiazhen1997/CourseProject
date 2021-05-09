
import math
import sys

__author__ = 'Daniel'


class Solution(object):
    F = [0]  

    def numSquares(self, n):
        
        while len(Solution.F) <= n:
            i = len(Solution.F)
            Solution.F.append(sys.maxint)
            j = 1
            while i - j*j >= 0:
                Solution.F[i] = min(Solution.F[i], Solution.F[i-j*j]+1)
                j += 1

        return Solution.F[n]

    def numSquares_bfs(self, n):
        
        q = [0]
        visited = [False for _ in xrange(n+1)]

        level = 0
        while q:
            level += 1
            l = len(q)
            for i in xrange(l):
                for j in xrange(1, int(math.sqrt(n))+1):
                    nxt = q[i]+j*j
                    if nxt <= n and visited[nxt]:
                        continue
                    elif nxt < n:
                        visited[nxt] = True
                        q.append(nxt)
                    elif nxt == n:
                        return level
                    else:
                        break
            q = q[l:]

        return None

    def numSquares_TLE(self, n):
        
        F = [i for i in xrange(n+1)]
        for i in xrange(1, n+1):
            for j in xrange(1, int(math.sqrt(i))+1):
                if i-j*j >= 0:
                    F[i] = min(F[i], F[i-j*j]+1)

        return F[n]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""n""u""m""S""q""u""a""r""e""s""(""6"")"" ""=""="" ""3