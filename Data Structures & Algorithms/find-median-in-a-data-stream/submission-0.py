class MedianFinder:

    def __init__(self):
        self.arr=[]

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        num = self.arr
        if len(num) % 2 == 1:
            return num[(len(num) - 1) // 2]
        else:
            return (num[(len(num) - 1) // 2] + num[(len(num) - 1) // 2 + 1]) / 2
        