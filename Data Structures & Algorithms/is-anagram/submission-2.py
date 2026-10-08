from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = defaultdict(int)
        for i, char in enumerate(s):
            countS[char] += 1
            countS[t[i]] -= 1
        
        for v in countS.values():
            if v != 0:
                return False
        
        return True
            