class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        
        res = [0, 1]
        current_block_size = 2
        current_position = 0
        for i in range(2, n+1):

            res.append(res[current_position]+1)

            current_position +=1
            if current_position == current_block_size:
                current_position = 0
                current_block_size *=2
        
        return res


