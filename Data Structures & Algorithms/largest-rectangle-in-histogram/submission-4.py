class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        res = 0
        def loop(heights):
            nonlocal res
            stack = [] #(index, height)
            
            for i, h in enumerate(heights):
                j = i
                while stack and h < stack[-1][1]:
                    j, k = stack.pop()
                    res = max(res, (i - j)*k)
                    print(res)
                stack.append((j, h))
                print(stack)
            # while stack:
            #     j, k = stack.pop()
            #     res = max(res, (len(heights) - j)*k)
        loop(heights)
        loop(heights[::-1])
        return res