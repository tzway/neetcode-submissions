class Solution:
    # brute force
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                area = max(
                    area,
                    (j - i + 1) * min(heights[i:j+1])
                )
        return area