from functools import reduce
from operator import mul
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        have_zero = False
        product = 1
        for n in nums:
            if n == 0:
                have_zero = True
                continue
            product *= n
        
        if not have_zero:
            return 0
        
        complete_product = reduce(mul, range(1,len(nums)+1), 1)
        return complete_product // product