from types import MethodType
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        class MyMatrix(list):
            def get(self, i):
                n = len(self[0])
                return self[i//n][i%n]
        mtrx = MyMatrix(matrix)

        l, r = 0, len(matrix) * len(matrix[0]) - 1

        while l <=r:
            m = (l + r) // 2
            mVal = mtrx.get(m)
            if mVal == target:
                return True
            elif mVal < target:
                l = m +1
            else:
                r = m - 1
        return False