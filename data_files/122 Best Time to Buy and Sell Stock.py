
__author__ = 'Danyang'


class Solution(object):
    def maxProfit(self, A):
        
        if len(A) <= 1:
            return 0

        n = len(A)
        F = [0 for _ in xrange(n+1)]
        maxa = 0
        for i in xrange(2, n+1):
            F[i] = max(F[i-1] + A[i-1] - A[i-2], 0)  
            maxa = max(maxa, F[i])

        return maxa

    def maxProfitDelta(self, prices):
        
        if len(prices) <= 1:
            return 0
        delta_prices = []
        for i in xrange(1, len(prices)):
            delta_prices.append(prices[i]-prices[i-1])

        
        
        max_sub_array = 0
        current_sub_array = 0
        for j in xrange(len(delta_prices)):
            current_sub_array = max(0, current_sub_array+delta_prices[j])
            max_sub_array = max(max_sub_array, current_sub_array)

        return max_sub_array


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""P""r""o""f""i""t""(""[""3"","" ""2"","" ""1"","" ""4"","" ""5"","" ""6"","" ""2""]"")"" ""=""="" ""5