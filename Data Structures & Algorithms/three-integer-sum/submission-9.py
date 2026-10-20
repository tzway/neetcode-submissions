class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = set()

        for i in range(len(nums)-2):
            a = nums[i]
            if a > 0:
                break
            j, k = i+1, len(nums) - 1
            while j < k:
                b, c = nums[j], nums[k]
                if a + b + c == 0:
                    result.add((a,b,c))
                    j +=1
                    k -=1
                elif a + b + c < 0:
                    j += 1
                elif a + b + c > 0:
                    k -=1
        
        return list(result)