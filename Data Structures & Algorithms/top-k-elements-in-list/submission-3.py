from collections import Counter
from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        minHeap = []
        for number, fq in freq.items():
            heappush(minHeap, (fq, number))
            if len(minHeap) > k:
                heappop(minHeap)
        return [number for fq, number in minHeap]