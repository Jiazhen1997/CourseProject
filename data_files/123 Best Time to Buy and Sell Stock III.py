
__author__ = 'Danyang'


class Solution:
    def maxProfit(self, prices):
        
        if len(prices) <= 1:
            return 0

        
        forward = [0 for _ in xrange(len(prices))]  
        lowest_buy_price = prices[0]
        for i in xrange(1, len(prices)):
            
            
            
            forward[i] = max(forward[i-1], prices[i]-lowest_buy_price)

            lowest_buy_price = min(prices[i], lowest_buy_price)

        backward = [0 for _ in xrange(len(prices))]  
        highest_sell_price = prices[-1]
        for i in xrange(len(prices)-2, -1, -1):
            
            
            
            backward[i] = max(backward[i+1], highest_sell_price-prices[i])

            highest_sell_price = max(prices[i], highest_sell_price)

        max_profit = 0
        for i in xrange(len(prices)):
            max_profit = max(max_profit, forward[i]+backward[i])
        return max_profit

    def maxProfit_error(self, prices):
        

        if len(prices) <= 1:
            return 0

        delta_prices = []
        for i in xrange(1, len(prices)):
            delta_prices.append(prices[i]-prices[i-1])

        
        max_profits = [0, 0]

        max_sub_array = 0
        current_sub_array = 0
        for j in xrange(len(delta_prices)):
            if current_sub_array+delta_prices[j] >= 0:
                current_sub_array += delta_prices[j]
                max_sub_array = max(max_sub_array, current_sub_array)
            else:
                
                if max_sub_array > max_profits[0]:
                    max_profits[1] = max_profits[0]
                    max_profits[0] = max_sub_array
                elif max_sub_array > max_profits[1]:
                    max_profits[1] = max_sub_array
                max_sub_array = 0
                current_sub_array = 0

        return sum(max_profits)
