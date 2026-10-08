class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def isWater(coordinate):
            r, c = coordinate
            if not 0<=r < len(grid) or not 0<=c < len(grid[0]):
                return True
            if grid[r][c] == 0:
                return True
            return False

        def bfs(origin):
            visit = set()
            q = deque()
            q.append(origin)
            visit.add(origin)
            all_visit.add(origin)

            while q:
                for i in range(len(q)):
                    r, c = q.popleft()

                    directions = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
                    for direction in directions:
                        if isWater(direction) or direction in visit:
                            continue
                        visit.add(direction)
                        all_visit.add(direction)
                        q.append(direction)
            print(visit)
            return len(visit)
        
        all_visit = set()
        res=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if isWater((r,c)) or (r,c) in all_visit:
                    continue
                res = max(res,bfs((r,c)))
        return res