class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        track = []
        def backtrack(start):
            if sum(track) == target:
                res.append(track.copy())
                return
            if sum(track) > target:
                return

            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(i)
                track.pop()
            return
        backtrack(0)
        print(res)
        return res
        
            