from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for n in nums:
            heappush(minHeap, n)
            if len(minHeap) > k:
                heappop(minHeap)
        return minHeap[0]