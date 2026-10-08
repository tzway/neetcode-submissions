class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCntr = Counter(t)
        string = None
        def rec(s):
            nonlocal string
            if not tCntr <= Counter(s):
                return
            if string is None or len(s) < len(string):
                string = s
            
            rec(s[:-1])
            rec(s[1:])
        
        rec(s)
        return string if string else ""