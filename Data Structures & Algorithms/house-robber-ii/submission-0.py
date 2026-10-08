
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def get_max_money(nums, left, right):
            if left == right:
                return nums[left]
            if (right - left)%len(nums) == 1:
                return max(nums[left], nums[right])
            if (left, right) in memo:
                return memo[(left, right)]
            money = 0
            middle = (left + 1)%len(nums)
            while middle%len(nums) != right%len(nums):
                leftMoney = get_max_money(nums, left ,(middle-1)%len(nums))
                rightMoney = get_max_money(nums, (middle + 1)%len(nums), right)
                money = max(money, leftMoney + rightMoney)
                middle = (middle + 1)%len(nums)
            memo[(left,right)] = money
            return money
        
        money = 0
        for i in range(len(nums)):
            money = max(money, get_max_money(nums, i, (i-2)%len(nums)))
        
        return money