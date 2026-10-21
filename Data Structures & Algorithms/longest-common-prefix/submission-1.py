class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_arr = []
        for chars in zip(*strs):
            if len(set(chars)) != 1:
                break
            prefix_arr.append(chars[0])
        
        return "".join(prefix_arr)