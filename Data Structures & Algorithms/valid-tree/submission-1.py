class UF:
    # 连通分量个数
    _count: int
    # 存储每个节点的父节点
    parent: List[int]

    # n 为图中节点的个数
    def __init__(self, n: int):
        self._count = n
        self.parent = [i for i in range(n)]

    # 将节点 p 和节点 q 连通
    def union(self, p: int, q: int):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return

        self.parent[rootQ] = rootP
        # 两个连通分量合并成一个连通分量
        self._count -= 1

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
        return self._count
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UF(n)
        for i, j in edges:
            if uf.connected(i,j):
                return False
            uf.union(i,j)
        
        return uf.count() == 1
