class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_arr = [i for i in board if 'R' in i]
        rook = rook_arr[0].index('R')
        x = [i[rook] for i in board]
        can_mov = [x[:x.index('R')][::-1], x[x.index('R') + 1:], rook_arr[0][:rook][::-1], rook_arr[0][rook + 1:]]
        count = 0
        print(can_mov)
        for mov in can_mov:
            for step in mov:
                if step.isupper():
                    break
                if step == 'p':
                    count += 1
                    break

        return count
