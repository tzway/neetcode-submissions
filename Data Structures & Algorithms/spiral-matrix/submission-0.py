class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)] # r d l u
        visited = set()
        def traverse():
            output = []
            r, c = 0, 0
            direction = 0
            while len(visited) < len(matrix) * len(matrix[0]):
                output.append(matrix[r][c])
                visited.add((r,c))
                dr, dc = deltas[direction]
                nr, nc = r + dr, c + dc

                if (nr,nc) in visited or nr< 0 or nc < 0 or nr>= len(matrix) or nc >= len(matrix[0]):
                    direction = (direction + 1) % 4
                    dr, dc = deltas[direction]
                    nr, nc = r + dr, c + dc

                r, c = nr, nc
            
            return output
        
        return traverse()