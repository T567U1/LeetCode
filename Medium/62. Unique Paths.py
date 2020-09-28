class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0] * m] * n
        matrix[0] = [1] * m
        for i, row in enumerate(matrix[1:]):
            matrix[i + 1] = [i + j for i, j in zip(matrix[i], matrix[i + 1])]
            row = matrix[i + 1][:]
            t = 1
            for j in range(1, len(row)):
                row[j] += t
                t = row[j]
            matrix[i + 1] = row[:]

        return matrix[-1][-1]
