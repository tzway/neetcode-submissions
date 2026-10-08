class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        countList = [0 for i in range(26)]
        get_i = lambda x: ord(x) - ord('A')

        maxCount = 0
        while r < len(s):
            print(countList)
            
            
            countList[get_i(s[r])] += 1
            
            while sum(countList) - max(countList) > k:
                countList[get_i(s[l])] -= 1
                l +=1
            maxCount = max(maxCount, r-l+1)

            r += 1
    
        return maxCount

