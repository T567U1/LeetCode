class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = []
        for x, y in zip(board, list(zip(*board))):
            #for latter used matrix
            m += [x[i: i + 3] for i in range(0, len(board[0]), 3)],
            x1 = collections.Counter(x)
            y1 = collections.Counter(y)
            #check for duplicates on the x axis
            for i in x1:
                if i.isdigit():
                    if x1[i] > 1:
                        return False
            #check for duplicates on the y axis
            for i in y1:
                if i.isdigit():
                    if y1[i] > 1:
                        return False

        #make a 3 * 3 matrix of a matrix
        for i in range(0, len(board[0]), 3):
            for x, y, z in zip(m[i + 0], m[i + 1], m[i + 2]):
                c = collections.Counter(x + y + z)
                for i in c:
                    if i.isdigit():
                        if c[i] > 1:
                            return False
        return True
