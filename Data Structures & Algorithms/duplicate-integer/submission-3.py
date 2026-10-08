class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tempnums = nums[:]
        for num in nums:
            tempnums.remove(num)
            for tempnum in tempnums:
                if num == tempnum:
                    return True
        return False
         