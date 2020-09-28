class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])
        # count number of 1's to the left
        # row[i][col[i]] = number of 1 to the left - 1
        for r, row in enumerate(mat):
            for c, v in enumerate(row):
                if v and c:
                    mat[r][c] += mat[r][c -1]
        # min would be the limeter for the rectangle if 0 it wont matter
        ans = 0
        for r1 in range(R):
            for c1 in range(C):
                m = mat[r1][c1]
                for r2 in range(r1, R):
                    m = min(m, mat[r2][c1])
                    ans += m

        return ans
