class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]
        res = 0
        stack = [] #(index, height)
        
        for i, h in enumerate(heights):
            j = i
            while stack and h < stack[-1][1]:
                j, k = stack.pop()
                res = max(res, (i - j)*k)

            stack.append((j, h))

        return res