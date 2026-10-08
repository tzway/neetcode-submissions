class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = list()
        track= []
        
        def backtrack(subsets, start, nums):
            print(track, start)
            subsets.append(track[:])
            
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(subsets, i + 1, nums)
                track.pop()

        backtrack(subsets, 0, nums)
        return subsets


