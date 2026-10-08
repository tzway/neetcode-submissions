class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_all = 1
        zero_count = 0
        zero_index = None
        for i, num in enumerate(nums):
            if num == 0:
                zero_count +=1
                zero_index = i
                continue
            product_all *= num

        if zero_count > 1:
            return [0] * len(nums)
        if zero_count == 1:
            res = [0]* len(nums)
            res[zero_index] = product_all
            return res
        return [product_all//num for num in nums]
