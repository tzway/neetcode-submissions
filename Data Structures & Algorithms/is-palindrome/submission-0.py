class Solution:
    def isPalindrome(self, s: str) -> bool:

        s2 = []
        for c in s:
            if c.isalnum():
                s2.append(c.lower())
        
        i = 0
        while i<len(s2)-i-1:
            if s2[i] != s2[len(s2)-i-1]:
                return False
            i +=1
        return True