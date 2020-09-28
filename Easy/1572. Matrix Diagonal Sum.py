class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0

        for i, x in enumerate(mat):
            ans += x[i]
            mat[i][i] = 0


        for i, y in enumerate(mat[::-1]):
            ans += y[i]

        return ans


            
