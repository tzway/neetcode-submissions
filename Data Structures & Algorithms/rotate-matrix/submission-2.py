from math import ceil, floor
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # nr, nc = c, len(matrix) - 1 - r
        def get_next(r,c):
            return c, len(matrix) - 1 - r



        for r in range(ceil(len(matrix)/2)):
            for c in range(floor(len(matrix)/2)):
                
                r1, c1 = get_next(r,c)
                r2, c2 = get_next(r1,c1)
                r3, c3 = get_next(r2,c2)
                print(matrix[r][c], matrix[r1][c1], matrix[r2][c2], matrix[r3][c3])
                matrix[r][c], matrix[r1][c1], matrix[r2][c2], matrix[r3][c3] = matrix[r3][c3], matrix[r][c], matrix[r1][c1], matrix[r2][c2]
        

                

