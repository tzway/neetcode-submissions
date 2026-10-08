class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s):
            if len(s) == 2*n:
                res.append(s)
                return
            
            openCount = s.count("(")
            closeCount = s.count(")")
            if closeCount < openCount < n:
                backtrack(s+"(")
                backtrack(s+")")
            elif closeCount < openCount == n:
                backtrack(s+")")
            elif closeCount == openCount:
                backtrack(s+"(")

        backtrack("")
        return res