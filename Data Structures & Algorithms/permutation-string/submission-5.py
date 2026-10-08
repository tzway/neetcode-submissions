class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr1 = Counter(s1)
        cntr2 = Counter(s2[:len(s1)])
        if cntr1 == cntr2:
            return True
        for r in range(len(s1), len(s2)):
            cntr2[s2[r]] += 1
            cntr2[s2[r-len(s1)]] -= 1
            if cntr1 == cntr2:
                return True

        return False