
__author__ = 'Danyang'


class Solution:
    def maxProfit(self, prices):
        
        if len(prices) <= 1:
            return 0

        delta_prices = []  
        for i in xrange(1, len(prices)):
            delta_prices.append(prices[i]-prices[i-1])

        
        profit = 0
        for i in xrange(len(delta_prices)):
            if delta_prices[i] > 0:
                profit += delta_prices[i]

        return profit