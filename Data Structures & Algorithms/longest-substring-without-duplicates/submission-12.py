class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        chars = set()
        res = 0
        for r, c in enumerate(s):
            while c in chars:
                chars.remove(s[l])
                l +=1
            chars.add(c)
            res = max(len(chars), res)
        return res