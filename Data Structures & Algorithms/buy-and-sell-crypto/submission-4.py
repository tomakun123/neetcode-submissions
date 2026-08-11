class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for buy in range(len(prices)):
            for sell in range(buy+1,len(prices)):
                profit = prices[sell] - prices[buy]
                if profit > maxProfit:
                    maxProfit = profit
        
        return maxProfit
