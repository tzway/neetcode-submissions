class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        lowest_price = prices[0]

        for price in prices:
            lowest_price = min(lowest_price, price)
            maxProfit = max(price -lowest_price, maxProfit)
        return maxProfit
            

        