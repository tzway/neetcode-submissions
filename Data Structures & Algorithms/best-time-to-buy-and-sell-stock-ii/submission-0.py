class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit = 0
        cost = prices[0]
        for price in prices:
            if price > cost:
                profit += price - cost
            cost = price

            if price < cost:
                cost = price
        return profit