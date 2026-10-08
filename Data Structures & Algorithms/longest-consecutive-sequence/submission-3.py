class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        big = nums[0]
        small = nums[0]
        for n in nums:
            if big < n:
                big = n
            if small > n:
                small = n

        buckets = [False]* (big - small+1) 

        for n in nums:
            buckets[n - small] = True
        
        res = 1
        streak = 0
        for b in buckets:
            if b:
                streak +=1
            else:
                streak = 0
            if streak> res:
                res = streak
        
        return res


