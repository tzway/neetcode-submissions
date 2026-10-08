class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        res = []
        for i, n in enumerate(nums):
            heapq.heappush(maxHeap, (-n, i))
            if i < k - 1:
                continue
            while maxHeap[0][1] <= i - k:
                heapq.heappop(maxHeap)
            res.append(-maxHeap[0][0])
        return res