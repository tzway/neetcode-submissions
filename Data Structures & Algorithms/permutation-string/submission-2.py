from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr = Counter(s1)
        for i in range(len(s2)):
            if Counter(s2[i:i+len(s1)]) == cntr:
                return True
        
        return False