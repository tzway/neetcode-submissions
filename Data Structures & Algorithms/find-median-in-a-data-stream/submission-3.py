from heapq import *


class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        if self.minheap and num > self.minheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -1 * num)
        self.rebalance()
    
    def rebalance(self) -> None:
        while len(self.minheap) > len(self.maxheap):
            heappush(self.maxheap, -heappop(self.minheap))
        while len(self.minheap) < len(self.maxheap):
            heappush(self.minheap, -heappop(self.maxheap))
        # print(self.minheap, self.maxheap)

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        elif len(self.maxheap) < len(self.minheap):
            return self.minheap[0]
        else:
            return (self.minheap[0] - self.maxheap[0]) / 2

        
        