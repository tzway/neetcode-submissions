class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def isOutBound(r,c):
            return r<0 or c <0 or r>=len(board) or c >= len(board[0])

        visited = set()
        deltas = [(0,1),(1,0),(-1,0),(0,-1)]
        def bfs(origin):
            live = False
            thisVisited = set([origin])
            q = deque([origin])
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in deltas:
                        nr, nc = r+dr, c+dc
                        if isOutBound(nr,nc):
                            live = True
                            continue
                        if (nr,nc) in thisVisited:
                            continue
                        if board[nr][nc] == 'X':
                            continue
                        
                        q.append((nr,nc))
                        thisVisited.add((nr,nc))
            
            visited.update(thisVisited)
            if not live:
                for r, c in thisVisited:
                    board[r][c] = 'X'

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O' and (r,c) not in visited:
                    bfs((r,c))
        
        
