from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def isPalindrome(self, s):
        return s == s[::-1]

    @lru_cache(maxsize=None)
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        if self.isPalindrome(s):
            return s

        res = s[0]

        for i in range(1, len(s)):
            l = self.longestPalindrome(s[:i])
            r = self.longestPalindrome(s[i:])
            res = max(res, l, r, key=len)
        
        return res
