class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        track = []
        res = []
        def backtrack(start):
            res.append(track.copy())
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                track.append(nums[i])
                backtrack(i+1)
                track.pop()
        backtrack(0)
        return res
            
        