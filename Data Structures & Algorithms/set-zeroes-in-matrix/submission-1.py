class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # Step 1: mark rows and cols
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        # Step 2: use markers to set zeroes
        for r in range(1, ROWS):
            for c in range(1, COLS):   # start at 1 to avoid overwriting markers
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Step 3: handle first column
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # Step 4: handle first row
        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0
