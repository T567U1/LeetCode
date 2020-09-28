class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        #my answer
        matrix_ = []
        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            matrix_.append(max(temp))

        ans = []
        for i in matrix:
            i_ = i.index(min(i))
            if min(i) == matrix_[i_]:
                ans.append(matrix_[i_])

        return ans

        #Help from awise
        x = list(map(min, matrix))
        y = list(map(max, zip(*matrix)))

        ans = []
        for r, row in enumerate(matrix):
            for i, val in enumerate(row):
                if val == x[r] == y[i]:
                    ans.append(val)
        return ans

        #one liner
        return list({min(row) for row in matrix} & {max(col) for col in zip(*matrix)})
