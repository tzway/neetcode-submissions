class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        subString = ''
        for c in s:
            
            if c not in subString:
                subString += c
                print(subString)
                maxLength = max(len(subString),maxLength)
            else:
                i_dup = subString.index(c)
                subString = subString[i_dup+1:]
                subString += c

        
        return maxLength