from functools import reduce
class Solution:
    def isHappy(self, n: int) -> bool:
        track = set()
        while n != 1:
            track.add(n)
            digits = list(str(n))
            n = reduce(lambda x, y: x + int(y)**2, digits ,0)
            if n in track:
                return False
        return True