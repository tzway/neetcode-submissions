class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        n_str = ""
        res = []
        i = 0
        while i < len(s):
            print(n_str)
            c = s[i]
            if c == "#":
                n = int(n_str)
                res.append(s[i+1:i+1+n])
                i +=n
                n_str = ""
            else:
                n_str += c
            i +=1
        return res

            