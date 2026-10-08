class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        r = 0

        get_i = lambda x: ord(x)-ord('a')
        needToMatch = [0 for _ in range(26)]
        currentCount = needToMatch[:]

        for c in s1:
            needToMatch[get_i(c)] +=1

    
        while r < len(s2):
            currentCount[get_i(s2[r])] += 1
            
            if currentCount == needToMatch:
                return True

            if r - l >= len(s1) -1:
                currentCount[get_i(s2[l])] -= 1
                l +=1
            r +=1
            

            print(currentCount)
            print(l,r)
            print(s2[l:r+1])

        return False
