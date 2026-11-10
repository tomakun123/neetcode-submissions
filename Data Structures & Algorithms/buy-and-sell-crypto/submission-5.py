class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        low_i = 0
        high_i = len(prices)-1
        while ( low_i <= high_i ):
            est = prices[high_i] - prices[low_i]
            if est > prof:
                prof = est
            high_i -= 1
            if high_i == low_i:
                high_i = len(prices)-1
                low_i += 1
        return prof
            