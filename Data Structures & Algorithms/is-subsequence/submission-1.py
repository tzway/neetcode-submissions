class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not set(s).issubset(set(t)):
            return False
        
        i = 0
        for c in t:
            if i >= len(s):
                break
            if c == s[i]:
                i +=1

        return i >=len(s)