class Solution:
    def trap(self, height: List[int]) -> int:
        # from 0 to i
        leftMax = [max(height[:i+1]) for i in range(len(height))]
        # from i to -1
        rightMax = [max(height[i:]) for i in range(len(height))]
        print(leftMax)
        print(rightMax)

        return sum(
            min(leftMax[i], rightMax[i]) - height[i] for i in range(len(height))
            )

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         if n == 0:
#             return 0
        
#         leftMax = [0] * n
#         rightMax = [0] * n
        
#         leftMax[0] = height[0]
#         for i in range(1, n):
#             leftMax[i] = max(leftMax[i - 1], height[i])
        
#         rightMax[n - 1] = height[n - 1]
#         for i in range(n - 2, -1, -1):
#             rightMax[i] = max(rightMax[i + 1], height[i])
        
#         print(leftMax)
#         res = 0
#         for i in range(n):
#             res += min(leftMax[i], rightMax[i]) - height[i]
#         return res