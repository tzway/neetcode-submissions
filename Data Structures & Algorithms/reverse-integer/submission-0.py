class Solution:
    def reverse(self, x: int) -> int:
        highBound = 2**31 -1
        lowBound = -2**31

        res = str(x)[::-1]
        if res[-1] == '-':
            res = - int(res[:-1])
        else:
            res = int(res)
        return res if lowBound <= res <= highBound else 0