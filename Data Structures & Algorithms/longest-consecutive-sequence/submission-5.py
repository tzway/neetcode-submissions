class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        length = 0
        for n in nums:
            thisLength = 1
            while n + 1 in nums:
                thisLength += 1
                n +=1
            length = max(length, thisLength)

        return length
