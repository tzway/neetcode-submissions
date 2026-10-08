class Solution:
    def climbStairs(self, n: int) -> int:
        def bf(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            return bf(n-1) + bf(n-2)
        return bf(n)