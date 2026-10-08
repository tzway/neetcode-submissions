class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def contains_dup(l):
            hashmap = set()
            for n in l:
                if n in hashmap:
                    return True
                if n != '.':
                    hashmap.add(n)
            return False
        
        def get_col(i):
            col = []
            for j in range(9):
                col.append(board[j][i])
            return col
        
        def get_cube(i,j):
            cube = []
            for k in range(3):
                for l in range(3):
                    cube.append(board[i+k][j+l])
            return cube

        for row in board:
            if contains_dup(row):
                return False

        
        for i in range(9):
            col = get_col(i)
            if contains_dup(col):
                return False
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                cube = get_cube(i,j)
                if contains_dup(cube):
                    return False

        return True