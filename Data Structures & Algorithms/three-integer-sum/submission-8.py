class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = set()

        for i in range(len(nums)-2):
            j, k = i+1, len(nums) - 1
            while j < k:
                a, b, c = nums[i], nums[j], nums[k]
                if a + b + c == 0:
                    result.add((a,b,c))
                    j +=1
                    k -=1
                elif a + b + c < 0:
                    j += 1
                elif a + b + c > 0:
                    k -=1
        
        return list(result)