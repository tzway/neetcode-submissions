class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product_all = 1
        # for num in nums:
        #     product_all *= num
        # return [product_all//num for num in nums]
        res = []
        for i, n in enumerate(nums):
            prod = 1
            for j, n in enumerate(nums):
                if j == i:
                    continue
                prod *= nums[j]
            res.append(prod)
        return res
