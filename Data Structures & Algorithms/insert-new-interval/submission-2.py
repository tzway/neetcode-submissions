class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = newInterval
        res = []
        idx = 0
        for i, j in intervals:
            if j < left:
                res.append([i,j])
                idx +=1
            elif i> right:
                res.append([i,j])
            else:
                if i<= left:
                    left =i
                if j >= right:
                    right =j
        
        res.insert(idx,[left,right])
        return res