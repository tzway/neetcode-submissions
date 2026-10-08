class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            j, k = i + 1, len(nums) -1
            while j < k < len(nums):
                ijkSum = nums[i] + nums[j] + nums[k]
                if ijkSum == 0:
                    res.add((nums[i],nums[j],nums[k]))
                    j +=1
                elif ijkSum > 0:
                    k -= 1
                elif ijkSum < 0:
                    j += 1
        return [list(e) for e in res]