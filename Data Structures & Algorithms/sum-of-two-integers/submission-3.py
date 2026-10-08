import math
class Solution:
    def getSum(self, a: int, b: int) -> int:
        powA = 2 ** a
        powB = 2 ** b

        return int(math.log(powA * powB, 2))
