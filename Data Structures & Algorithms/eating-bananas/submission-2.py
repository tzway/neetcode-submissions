from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k = ceil(sum(piles)/h)
        while True:
            t = 0
            for pile in piles:
                t +=ceil(pile/k)
                if t >h:
                    break
            if t <=h:
                return k
            k +=1
        
