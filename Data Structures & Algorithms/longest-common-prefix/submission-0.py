class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res_list = []
        for chars in zip(*strs):
            if len(set(chars)) > 1:
                break
            res_list.append(chars[0])
        return "".join(res_list)