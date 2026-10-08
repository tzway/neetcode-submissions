class UF:
    def __init__(self, n: int):
        # 连通分量个数
        self.count_ = n
        # 存储每个节点的父节点
        self.parent = [i for i in range(n)]
  
    # 将节点 p 和节点 q 连通
    def union(self, p: int, q: int) -> None:
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return

        self.parent[rootQ] = rootP
        # 两个连通分量合并成一个连通分量
        self.count_ -= 1

    # 判断节点 p 和节点 q 是否连通
    def connected(self, p: int, q: int) -> bool:
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # 返回图中的连通分量个数
    def count(self) -> int:
        return self.count_
def get_distance(listOfPoints):
    x0, y0 = listOfPoints[0]
    x1, y1 = listOfPoints[1]
    return abs(x0 - x1) + abs(y0 - y1)
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        uf = UF(len(points))
        edges = []
        for p0 in points:
            for p1 in points:
                if p0 == p1:
                    continue
                edges.append([p0,p1])
        edges.sort(key=get_distance)
        
        cost = 0
        for p0, p1 in edges:
            i0, i1 = points.index(p0), points.index(p1)
            if uf.connected(i0, i1): continue
            if uf.count == 1: break
            uf.union(i0, i1)
            cost += get_distance([p0, p1])
        
        return cost
        