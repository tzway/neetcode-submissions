class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_index = {}
        for i, n in enumerate(nums):
            if target - n in val_index:
                return [val_index[target - n], i]
            val_index[n] = i
