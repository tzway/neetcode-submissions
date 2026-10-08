class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        squares = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                digit = board[r][c]
                if digit != ".":

                    if digit in squares[(r // 3) * 3 + (c // 3)] or digit in rows[r] or digit in cols[c]:
                        return False
                    squares[(r // 3) * 3 + (c // 3)].add(digit)
                    rows[r].add(digit)
                    cols[c].add(digit)


        return True
                