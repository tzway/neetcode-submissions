class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(1,len(nums)-1):
            left = 0
            right = len(nums) - 1
            for left in range(0,i):
                for right in range(i+1,len(nums)):
                    if nums[left] + nums[i] + nums[right] == 0:
                        triplet = [nums[left],nums[i],nums[right]]
                        triplet.sort()
                        if triplet not in res:
                            res.append(triplet)
        
        return res

            


        