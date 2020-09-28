class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x, y = len(matrix), len(matrix[0])
        for i, z in enumerate(zip(*matrix)):
            matrix[0][i] = z

        temp = matrix[0] + []

        for i in range(x):
            for j in range(y):
                matrix[i][j] = temp[i][j]
            matrix[i] = matrix[i][::-1]

        return matrix
