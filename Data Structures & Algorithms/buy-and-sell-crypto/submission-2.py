class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#what is the shit looking problem Approach-> firstly visit the array (no sorting allowed ) as it changes the order of prices sets per days.
#figure out the patter if it continues decreasing order , No profit only loss so avoide any trade
#if there is a increaseing order than only we can make any order.
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit
        
        
        
        
        
        
        
        
        # left = 0;
        # right = 1
        # profit = 0
        # decreasing_pattern = 1
        # for i in range(1, len(prices)):
        #     if prices[i-1] >= prices[i]:
        #      # avoide transaction
        #         continue
                
        #     else:
        #         decreasing_pattern = 0
        #         break
        # if decreasing_pattern == 0:
        #     while right < len(prices)-1:

        #         if prices[left] < prices[right]:
        #             profit = prices[right]- prices[left]
        #             right +=1
        #         else:
        #             left = right
        #             right+=1
                    
        # else:
        #         profit = 0

        # return profit