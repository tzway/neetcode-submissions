class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product_all = 1
        # for num in nums:
        #     product_all *= num
        # return [product_all//num for num in nums]
        res = []
        for i, n in enumerate(nums):
            j = 0
            prod = 1
            while j < len(nums):
                if j == i:
                    j +=1
                    continue
                prod *= nums[j]
                j +=1
            res.append(prod)
        return res
