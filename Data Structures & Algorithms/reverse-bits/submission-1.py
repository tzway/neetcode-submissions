class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        coef = 2 ** 31
        while n:
            res += (n%2)*coef
            coef //=2
            n //= 2
        return res
