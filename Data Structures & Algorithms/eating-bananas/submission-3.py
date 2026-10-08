from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_speed_enough(time, speed):
            total_time = 0
            for pile in piles:
                total_time += ceil(pile/speed)
                if total_time > time:
                    return False
            
            return True
        
        slow = 1
        fast = max(piles)


        while slow <= fast:
            middle = (slow+fast)//2

            if is_speed_enough(h, middle):
                res = middle
                fast = middle - 1
            else:
                slow = middle + 1
        return res
        



        
