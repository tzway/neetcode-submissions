class CountSquares:

    def __init__(self):
        self.matrix = [[0 for _ in range(1000)] for _ in range(1000)]
        print(len(self.matrix))
        print(len(self.matrix[0]))
        print(self.matrix[0][0])

    def add(self, point: List[int]) -> None:
        x, y = point
        self.matrix[x][y] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0
        matrix = self.matrix
        for x0 in range(1000):
            if x0 == x:
                continue
            if matrix[x0][y]:
                print(f"Point {(x0, y)} Value {matrix[x0][y]}")
                # square 1
                if 0<= x0-x+y <1000:
                    res += matrix[x0][y] * matrix[x][x0-x+y] * matrix[x0][x0-x+y]
                # square 2
                if 0<= x-x0+y <1000:
                    res += matrix[x0][y] * matrix[x][x-x0+y] * matrix[x0][x-x0+y]
        
        return res