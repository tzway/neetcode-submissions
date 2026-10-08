class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        tCntr = Counter(t)
        sCntr = Counter(s)
        l, r = 0, len(s) - 1

        res = ""

        while tCntr <= sCntr:
            res = s[l:r+1]
            sCntr[s[l]] -= 1
            l +=1

        l -= 1
        sCntr[s[l]] += 1
        
        while tCntr <= sCntr:
            res = s[l:r+1]
            sCntr[s[r]] -= 1
            r -=1

        print(res)
        
        return res