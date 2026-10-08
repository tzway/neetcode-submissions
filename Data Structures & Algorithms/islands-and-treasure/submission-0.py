class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        visited = set()
        track = set()

        def isWater(r,c):
            if not 0<= r < len(grid) or not 0<= c < len(grid[0]):
                return True
            if grid[r][c] == -1:
                return True
            return False

        def dfs(r,c, distance):
            if isWater(r,c):
                return
            if (r,c) in track:
                return
            
            # prune
            if 0< grid[r][c] <= distance:
                return
            
            grid[r][c] = min(distance, grid[r][c])

            directions = [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
            
            for a, b in directions:
                track.add((r,c))
                dfs(a,b, distance+1)
                track.remove((r,c))
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    dfs(r,c,0)
        
        print(track)
        
            


        