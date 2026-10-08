from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = None
        majority_count = 0
        num_count = defaultdict(int)

        for n in nums:
            num_count[n] += 1
            if num_count[n] > majority_count:
                majority = n
                majority_count = num_count[n]
        return majority