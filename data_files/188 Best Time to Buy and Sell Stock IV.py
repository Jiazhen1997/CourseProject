
__author__ = 'Daniel'


class Solution:
    def maxProfit(self, k, prices):
        
        n = len(prices)
        if k >= n:
            return self.maxProfit_unlimited_transactions(prices)

        l = [0 for _ in xrange(k+1)]  
        g = [0 for _ in xrange(k+1)]  
        gmax = 0
        for i in xrange(1, n):
            diff = prices[i] - prices[i-1]
            for j in xrange(k, 0, -1):
                l[j] = max(g[j-1]+diff, l[j]+diff)
                g[j] = max(l[j], g[j])
                gmax = max(gmax, g[j])

        return gmax

    def maxProfit_unlimited_transactions(self, prices):
        profit = 0
        for i in xrange(1, len(prices)):
            profit += max(0, prices[i] - prices[i-1])
        return profit

if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""P""r""o""f""i""t""(""2"","" ""[""1"","" ""2"","" ""4""]"")