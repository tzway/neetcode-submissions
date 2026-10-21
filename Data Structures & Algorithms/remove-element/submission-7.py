class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = len(nums) - 1, len(nums) -1

        while i >=0:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -=1
            i -=1
        return j + 1