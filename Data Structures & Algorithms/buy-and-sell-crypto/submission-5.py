class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        gprmax = 0

        while r < len(prices):
            profit = prices[r] - prices[l]

            if profit > 0:
                gprmax = max(gprmax, profit)
            else:
                l = r

            r += 1

        return gprmax
