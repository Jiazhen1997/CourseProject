
__author__ = 'Daniel'


class Solution:
    def copyBooks(self, pages, k):
        
        n = len(pages)
        s = [0 for _ in xrange(n+1)]
        for i in xrange(1, n+1):
            s[i] = s[i-1] + pages[i-1]

        F = [[s[j] for j in xrange(n+1)] for _ in xrange(k+1)]  

        for i in xrange(2, k+1):
            l = 0  
            r = 1  
            while r < n+1:
                F[i][r] = min(F[i][r],
                    max(F[i-1][l], s[r]-s[l])
                )
                if F[i-1][l] < s[r]-s[l] and l < r:
                    
                    l += 1
                else:
                    
                    if l > 0: l -= 1
                    r += 1

        return F[-1][-1]


class Solution_TLE:
    def copyBooks(self, pages, k):
        
        n = len(pages)
        s = [0 for _ in xrange(n+1)]
        for i in xrange(1, n+1):
            s[i] = s[i-1] + pages[i-1]

        F = [[s[j] for j in xrange(n+1)] for _ in xrange(k+1)]  

        for i in xrange(2, k+1):
            for j in xrange(1, n+1):
                F[i][j] = min(
                    max(F[i-1][t], s[j]-s[t]) for t in xrange(j)
                )

        return F[-1][-1]


class Solution_search:
    def copyBooks(self, pages, k):
        
        return self.bisect(pages, k, sum(pages)/k, sum(pages))

    def bisect(self, pages, k, lower, upper):
        
        while lower < upper:
            mid = (lower+upper)/2
            if self.valid(pages, k, mid):
                upper = mid
            else:
                lower = mid+1

        return lower

    def valid(self, pages, k, limit):
        cnt = 0
        k -= 1
        for p in pages:
            if p > limit: return False

            cnt += p
            if cnt > limit:
                cnt = p
                k -= 1

            if k < 0: return False

        return True


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""o""p""y""B""o""o""k""s""(""[""3"","" ""2""]"","" ""5"")"" ""=""="" ""3