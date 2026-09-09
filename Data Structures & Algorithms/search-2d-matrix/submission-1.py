class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False 
        row, cols = len(matrix), len(matrix[0]) 
        low, high = 0, row * cols - 1 

        while low <= high:
            mid = (low + high) // 2 
            row, col = divmod(mid, cols) # converts 1 d index into 2d
            val = matrix[row][col] 

            if val == target:
                return True 
            elif val < target:
                low = mid + 1 
            else : high = mid -1 
        return False