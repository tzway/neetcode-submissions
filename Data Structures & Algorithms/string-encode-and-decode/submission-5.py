class Solution:
# i reckon this problem can be solved by huffman encoding. can't do
    def encode(self, strs: List[str]) -> str:
        # the first few charaters are for the controlling purpose
        # the rest of the string are for the data storage
        # the first 2*200 space will be used for controlling
        res = ""
        for s in strs:
            if not s:
                res += "E"
            else:
                res += "R"
            res += str(len(s)).zfill(3)
        res =res.zfill(4*100)
        res += "".join(strs)
        return res

    def decode(self, s: str) -> List[str]:
        ctrl = s[:400]
        data = s[400:]
        res = []
        for i in range(0,400,4):
            if ctrl[i] == "E":
                res.append("")
                continue
            if ctrl[i] == "R":
                length = int(ctrl[i+1:i+4])
                res.append(data[:length])
                data = data[length:]
        return res


