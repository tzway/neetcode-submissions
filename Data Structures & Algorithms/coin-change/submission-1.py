class Solution:
    def __init__(self):
        self.memo = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.bf(coins, amount)
    
    def bf(self, coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        
        if amount in self.memo:
            return self.memo[amount]
        
        res = amount + 1
        for coin in coins:
            subProblem = self.bf(coins, amount - coin)
            if subProblem == -1:
                continue
            res = min(res, 1 + subProblem)
        
        self.memo[amount] = res if res <= amount else -1
        return self.memo[amount]
        