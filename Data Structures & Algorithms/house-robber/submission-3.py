
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def get_max_money(start):
            if start >= len(nums):
                return 0
            if len(nums) - start <= 2:
                return max(nums[start:])
            if start in memo:
                return memo[start]
            money1 = nums[start] + get_max_money(start + 2)
            money2 = nums[start + 1] + get_max_money(start + 3)
            money = max(money1, money2)
            
            memo[start] = money
            
            return money
        
        return get_max_money(0)
        