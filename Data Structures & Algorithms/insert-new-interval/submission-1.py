class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        res = []
        for i, j in intervals:
            if j < left:
                res.append([i,j])
            elif i> right:
                res.append([i,j])
            else:
                if i<= left:
                    left =i
                if j >= right:
                    right =j
        
        res.append([left,right])
        res.sort()
        return res