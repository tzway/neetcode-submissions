class Solution:

    def encode(self, strs: List[str]) -> str:
        tks = []
        for s in strs:
            tks.append(f"{len(s)}#")
            tks.append(s)
        res = "".join(tks)
        # print(res)
        return (res)
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            tk = ""
            while s[i].isalnum():
                tk += s[i]
                i +=1
            i +=1
            strs.append(s[i: i+int(tk)])
            i = i+int(tk)
        return strs