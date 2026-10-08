from collections import namedtuple
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]* len(temperatures)

        Record =namedtuple('Record', ['index','value'])
        for i, t in enumerate(temperatures):
            while stack and stack[-1].value < t:
                tmp = stack.pop()
                res[tmp.index] = i - tmp.index
            stack.append(Record(i,t))
        return res

        