class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keyMap = {
            '1':[],
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
            '0':['+'],
        }

        res = []
        track = ''

        def backtrack(remain):
            nonlocal track
            if not remain:
                if track:
                    res.append(track)
                return

            for character in keyMap[remain[0]]:
                track += character
                backtrack(remain[1:])
                track = track[:-1]

        backtrack(digits)

        print(res)
        return res

