class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        def findNext(temperatures):
            for i, t in enumerate(temperatures):
                if t > temperatures[0]:
                    return i
            return 0
        
        return [findNext(temperatures[i:]) for i in range(len(temperatures)) ]

        