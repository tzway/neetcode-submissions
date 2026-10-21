class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        res = 0
        for n in nums:
            if n - 1 in nums:
                continue
            init = n
            while n in nums:
                n +=1
            res = max(res, n - init)
        return res