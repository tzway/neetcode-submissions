class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length = 0
        for n in numSet:
            if n - 1 in numSet:
                continue
            thisLength = 1
            while n + 1 in numSet:
                thisLength +=1
                n +=1
            length = max(length, thisLength)
        
        return length

