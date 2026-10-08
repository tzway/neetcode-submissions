class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixList = [1] * len(nums)
        postfixList = [1] * len(nums)

        prefix = 1
        for i, n in enumerate(nums):
            prefixList[i] = prefix
            prefix *= n
            

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            postfixList[i] = postfix
            postfix *= nums[i]
            
        
        return [prefixList[i]* postfixList[i] for i in range(len(nums))]