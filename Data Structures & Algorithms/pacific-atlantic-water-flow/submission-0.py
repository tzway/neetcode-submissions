class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        flowPa = set()
        flowAt = set()
        
        deltas = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(r, c, visit):
            if (r,c) in visit:
                return
            
            visit.add((r,c))

            for dr, dc in deltas:
                nr, nc = r + dr, c + dc

                if nr < 0 or nc < 0 or nr>=len(heights) or nc >= len(heights[0]):
                    continue
                if heights[nr][nc] < heights[r][c]:
                    continue
                
                dfs(nr,nc, visit)
            return
        
        for c in range(len(heights[0])):
            dfs(0,c,flowPa)
            dfs(len(heights)-1,c,flowAt)
        for r in range(len(heights)):
            dfs(r,0,flowPa)
            dfs(r,len(heights[0])-1,flowAt)
        
        
        flowBoth = flowPa.intersection(flowAt)

        return [[r,c] for r,c in flowBoth]

