class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            print(stack)
            if not stack or t <= stack[-1][1]:
                stack.append((i,t))
                continue
            while stack and stack[-1][1] < t:
                j, s = stack.pop()
                res[j] = i - j
            stack.append((i,t))
        return res
            