
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def get_max_money(nums, left, right):
            if left > right:
                return 0
            if left == right:
                return nums[left]
            if right - left == 1:
                return max(nums[left:right+1])
            if (left, right) in memo:
                return memo[(left, right)]
            money = 0
            for middle in range(left, right+1):
                leftMoney = get_max_money(nums, left ,middle-1)
                rightMoney = get_max_money(nums, middle + 1, right)
                money = max(money, leftMoney + rightMoney)
            memo[(left,right)] = money
            return money
        return get_max_money(nums, 0, len(nums)-1)
        