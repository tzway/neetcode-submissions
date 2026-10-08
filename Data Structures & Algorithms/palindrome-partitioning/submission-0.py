class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(s):
            l, r = 0, len(s) -1
            while l < r:
                if s[l] != s[r]:
                    return False
                l +=1
                r -=1
            return True
        
        res = []
        track = []

        def backtrack(remain):
            if not remain:
                if track not in res:
                    res.append(track.copy())
                return
            
            border = 1
            while border<=len(s):
                print(f'in loop border is {border}')
                if is_palindrome(remain[:border]):
                    track.append(remain[:border])
                    print(track)
                    backtrack(remain[border:])
                    track.pop()
                border += 1
        
        backtrack(s)
        return res