class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        def go(row, col, ad, even):
            #print(row, col)
            if row < 0 or col > x:
                if even & 1:
                    self.ans += ad
                else:
                    self.ans += ad[::-1]
                return
            ad += matrix[row][col],
            go(row - 1, col + 1, ad, even)

        if not matrix:
            return matrix

        self.ans = []
        x = len(matrix[0]) - 1
        y = len(matrix) - 1

        for i in range(len(matrix)):
            ad = [matrix[i][0]]
            go(i - 1, 1, ad, i + 1)

        l = i - 1
        for i in range(1, len(matrix[0])):
            ad = [matrix[y][i]]
            go(y - 1, i + 1, ad, l + i)

        return self.ans
            
