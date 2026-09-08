from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # If the list is empty, no profit is possible
        if not prices:
            return 0
            
        # Initialize min_price to the first day's price
        min_price = prices[0]
        # Initialize max_profit to 0, as we can't have a negative profit
        max_profit = 0
        
        # Start iterating from the second day
        for i in range(1, len(prices)):
            current_price = prices[i]
            
            # 1. Update the minimum price seen so far (our best buying day)
            min_price = min(min_price, current_price)
            
            # 2. Calculate the potential profit if we sold today
            potential_profit = current_price - min_price
            
            # 3. Update the maximum profit found so far
            max_profit = max(max_profit, potential_profit)
            
        return max_profit