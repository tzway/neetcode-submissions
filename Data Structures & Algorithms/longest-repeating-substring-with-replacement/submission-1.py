from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        countMap = defaultdict(int)
        l, r = 0, 0
        while r < len(s):
            countMap[s[r]] +=1
            r +=1
            while k + max(countMap.values()) < sum(countMap.values()):
                countMap[s[l]] -=1
                l +=1
            res = max(res, r - l)

        return res
