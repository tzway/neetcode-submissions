class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLength = 0
        while r < len(s):
            if len(set(s[l:r+1])) == len(s[l:r+1]):
                maxLength = max(maxLength, len(s[l:r+1]))
                r +=1
            else:
                l +=1
        return maxLength