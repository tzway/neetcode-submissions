class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        deltas = [(0,1),(1,0),(0,-1),(-1,0)]

        def isEmpty(cell):
            r, c = cell
            if r<0 or r >= len(grid) or c<0 or c>= len(grid[0]):
                return True
            if grid[r][c] == 0:
                return True
            return False

        rotFruits = []
        bannas = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotFruits.append((r,c))
                if grid[r][c] == 1 or grid[r][c] == 2:
                    bannas +=1


        

        def bfs(rotFruits):
            time = 0
            q= deque(rotFruits)
            visited = set()
            print(rotFruits)

            while True:
                for _ in range(len(q)):
                    
                    r, c = q.popleft()
                    if isEmpty((r,c)) or (r,c) in visited:
                        continue
                    
                    visited.add((r,c))
                    
                    print((r,c))
                    for delta in deltas:
                        q.append((r+delta[0],c+delta[1]))
                    
                if len(visited) == bannas:
                    return time
                time +=1

                if not q:
                    break
            
            print(time)
            print(visited)
            return -1
        
        return bfs(rotFruits)


                    

