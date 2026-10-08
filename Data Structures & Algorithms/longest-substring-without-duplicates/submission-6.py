class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLength = 0
        while r <= len(s):
            if r - l == len(set(s[l:r])):
                maxLength = max(maxLength, r - l)
                r += 1
            else:
                l += 1
        return maxLength