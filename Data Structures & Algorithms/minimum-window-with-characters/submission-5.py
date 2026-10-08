class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        have = Counter()

        resLen = float('inf')
        res = ""

        l, r = 0, 0
        while r < len(s):
            while r < len(s) and not have >= need:
                have[s[r]] +=1
                r +=1
            
            while l <= r and have >= need:
                if r - l < resLen:
                    resLen = r - l
                    res = s[l:r]
                have[s[l]] -=1
                l +=1
        return res