import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(x**2+y**2,x, y) for (x,y) in points]
        heapq.heapify(points)
        res = []
        for _ in range(k):
            distance, x,y = heapq.heappop(points)
            res.append([x,y])
        return res