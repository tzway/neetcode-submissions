class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        
        print(res)

        return res
    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            for i, c in enumerate(s):
                if c == "#":
                    n = int(s[:i])
                    s = s[i+1:]
                    res.append(s[:n])
                    s = s[n:]
                    break
        return res
