class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_index = dict()

        for i, n in enumerate(nums):
            if n in complement_index:
                return [complement_index[n], i]
            complement_index[target-n] = i

