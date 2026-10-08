class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVolume = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                volume = min(heights[i],heights[j])* (j - i)
                maxVolume = max(volume, maxVolume)

        return maxVolume
        