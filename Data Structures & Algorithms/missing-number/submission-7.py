from functools import reduce
from operator import xor
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(xor, range(0, len(nums)+1), reduce(xor, nums))