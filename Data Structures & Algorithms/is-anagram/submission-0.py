class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        def createMap(s: str):
            d = dict()
            for c in s:
                if c in d.keys():
                    d[c] +=1
                else:
                    d[c] = 1
            return d
        
        return createMap(s) == createMap(t)