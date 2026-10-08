class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    for r1 in range(len(matrix)):
                        if matrix[r1][c] != 0: matrix[r1][c] = '0'
                    for c1 in range(len(matrix[0])):
                        if matrix[r][c1] != 0: matrix[r][c1] = '0'
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == '0':
                    matrix[r][c] = 0

        