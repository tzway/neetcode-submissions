class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums) - 1
            while j < k:
                if nums[i]+nums[j]+nums[k] > 0:
                    k -= 1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j += 1
                else:
                    triplet = [nums[i],nums[j],nums[k]]
                    if triplet not in res:
                        res.append(triplet)
                    k -=1
                    j +=1
        
        return res

        