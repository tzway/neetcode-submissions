class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = []
        exi = False
        track = []
        def backtrack(i,j,remain):
            nonlocal exi
            if not remain:
                res.append(track[:])
                exi = True
                return
            if not 0<=i<len(board) or not 0 <=j<len(board[0]):
                return
            if (i,j) in track:
                return
            if board[i][j] != remain[0]:
                return

            directions = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]

            for a, b in directions:
                track.append((i,j))
                backtrack(a,b,remain[1:])
                track.pop()
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(i,j,word)
                if exi:
                    return True
        print(res)
        return exi