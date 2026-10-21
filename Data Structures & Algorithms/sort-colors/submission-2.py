class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ct = Counter(nums)
        pointer = 0
        for i in range(3):
            for j in range(ct[i]):
                nums[pointer] = i
                pointer +=1
        