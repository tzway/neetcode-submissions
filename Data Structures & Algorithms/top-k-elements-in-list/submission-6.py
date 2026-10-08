class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val_freq = Counter(nums) # {1:1, 2:2, 3:3} # val:freq

        heap = []

        for val, freq in val_freq.items():
            heapq.heappush(heap, (freq, val))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [val for freq, val in heap]
        