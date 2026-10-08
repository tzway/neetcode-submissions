class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1
        while r < len(prices):
            margin = prices[r] - prices[l]
            if margin > 0:
                profit = max(profit, margin)
            else:
                l = r
            r += 1

        return profit