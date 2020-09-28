class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowl = len(matrix)
        coll = len(matrix[0])

        def go_row(row, col):
            if row == -1:
                return
            matrix[row][col] = 0
            return go_row(row - 1, col)

        def go_col(row, col):
            if col == -1:
                return
            matrix[row][col] = 0
            return go_col(row, col - 1)

        zeros = []

        # get zero's coordinates
        for x, row in enumerate(matrix):
            if 0 in row:
                for y, col in enumerate(row):
                    if not col:
                        zeros += (x, y),

        for x, y in zeros:
            go_row(rowl - 1, y)
            go_col(x, coll - 1)
