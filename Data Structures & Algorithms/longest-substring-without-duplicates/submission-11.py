class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hashset = set()
        res = 0
        for r, c in enumerate(s):
            if c not in hashset:
                hashset.add(c)
                res = max(res, len(hashset))
                continue
            if c in hashset:
                while s[l] != c:
                    hashset.remove(s[l])
                    l +=1
                l +=1
        return res