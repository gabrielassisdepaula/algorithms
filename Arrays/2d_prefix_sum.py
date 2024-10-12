class PrefixSum2D:

    def __init__(self, matrix: list[list[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        # add padding zeros to the matrix for edge cases
        self.prefix_sum = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for row in range(ROWS):
            row_prefix_sum = 0
            for col in range(COLS):
                # calculate the ONLY the row prefix sum, disregarding column sums
                row_prefix_sum += matrix[row][col]
                # get the sum of all the above values up to that column, accounting for padding zeros
                above = self.prefix_sum[row][col+1]
                # the current matrix pos has the value of it's row prefix sum + all the above up to that column
                # + ones to account for padding zeros
                self.prefix_sum[row+1][col+1] = row_prefix_sum + above
    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # all indexation accounting for padding zeros
        # get bottom right prefix sum 
        bottom_right = self.prefix_sum[row2+1][col2+1]
        # get prefix sum for the rows above our target area
        above = self.prefix_sum[row1][col2+1]
        # get prefix sum for the left columns of our target area
        left = self.prefix_sum[row2+1][col1]
        # get prefix sum for the above and left of our target area
        top_left = self.prefix_sum[row1][col1]
        # bottom_right contains our sum and more, so we subtract the left and above that is extra
        # and need to add the top left because it was subtracted two times (with above and left)
        return bottom_right - above - left + top_left