class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def isWater(r,c):
            if not 0<= r < len(grid) or not 0<= c < len(grid[0]):
                return True
            if grid[r][c] == -1:
                return True
            return False

        def bfs():

            distance = 0

            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    grid[r][c] = min(grid[r][c], distance)

                    directions = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]

                    for a, b in directions:
                        if isWater(a,b) or (a,b) in visited:
                            continue
                        q.append((a,b))
                        visited.add((a,b))
                
                distance +=1
        
        visited = set()
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        
        bfs()
