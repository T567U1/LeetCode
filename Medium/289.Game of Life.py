class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board) - 1
        n = len(board[0]) - 1

        def go(x, y, matrix):
            neigbors = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
            ans = 0
            for x1, y1 in neigbors:
                x2 = x + x1
                y2 = y + y1
                if x2 < 0 or x2 > m or y2 < 0 or y2 > n:
                    continue
                ans += board[x2][y2]
            if not board[x][y] and ans == 3:
                matrix[x][y] = 1

            elif board[x][y] and ans == 2 or ans == 3:
                matrix[x][y] = 1
            else:
                matrix[x][y] = 0

        matrix = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for x, i in enumerate(board):
            for y, j in enumerate(i):
                go(x, y, matrix)

        board[:] = matrix
