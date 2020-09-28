class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        x, x1 = min(row1, row2), min(col1, col2)
        y, y1 = max(row1, row2), max(col1, col2)
        ans = 0
        for i in range(x, y + 1):
            for j in range(x1, y1 + 1):
                ans += self.m[i][j]

        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
