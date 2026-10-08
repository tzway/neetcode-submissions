class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix:
            if matrix[0]:
                rows = len(matrix)
                cols = len(matrix[0])
            else: 
                return False
        else:
            return False
        
        left = 0
        right = rows*cols -1
        print(left)
        print(right)
        print(rows)
        print(cols)

        def get_row(index):
            return index // cols
            print(f"index: {index}row: {cols}")
        def get_col(index):
            return index % cols
            print(f"index: {index}col: {cols}")
        def get_val(index):
            return matrix[get_row(index)][get_col(index)]

        while left <= right:
            middle = (left + right) // 2
            val = get_val(middle)
            if val > target:
                right = middle -1
            elif val < target:
                left = middle + 1
            else:
                return True
        return False