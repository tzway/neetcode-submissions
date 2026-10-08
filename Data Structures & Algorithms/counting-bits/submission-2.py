class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        
        offset = 1
        next_offset = 2
        for i in range(1, n+1):
            if next_offset == i:
                offset = next_offset
                next_offset *= 2
            
            res[i] = 1 + res[i-offset]

        return res


