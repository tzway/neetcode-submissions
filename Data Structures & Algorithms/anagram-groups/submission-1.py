import string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        class stringPattern:
            lettersMap = {}
            for i, c in enumerate(string.ascii_lowercase):
                lettersMap[c] = i
            def __init__(self, s: str):
                self.ls = [0 for i in range(26)]
                for c in s:
                    self.ls[self.__class__.lettersMap[c]] +=1
        def getStringPattern(s):
            lettersMap = {}
            for i, c in enumerate(string.ascii_lowercase):
                lettersMap[c] = i
            ls = [0 for i in range(26)]
            for c in s:
                ls[lettersMap[c]] +=1
            return tuple(ls)
        
        patternMap = {}
        for s in strs:
            pattern = getStringPattern(s)
            if pattern not in patternMap:
                patternMap[pattern] = []
            patternMap[pattern].append(s)
        return patternMap.values()

        