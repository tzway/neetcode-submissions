
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {}
        def get_max_money(start, end):
            if start > end:
                return 0
            if end - start <= 1:
                return max(nums[start:end + 1])
            if (start, end) in memo:
                return memo[(start, end)]
            money1 = nums[start] + get_max_money(start + 2, end)
            money2 = nums[start + 1] + get_max_money(start + 3, end)
            money = max(money1, money2)
            
            memo[(start, end)] = money
            
            return money
        
        return max(get_max_money(0,len(nums)-2), get_max_money(1,len(nums)-1))
        