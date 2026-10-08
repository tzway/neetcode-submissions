from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        inv_nums = [-n for n in nums]
        heapify(inv_nums)
        res = None
        for _ in range(k):
            res = -heappop(inv_nums)
        return res
        