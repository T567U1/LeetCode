class Solution:
    def bitwiseComplement(self, N: int) -> int:
        rnum = ''
        for i in bin(N)[2:]:
            if i == '1':
                rnum += '0'
            else:
                rnum += '1'

        return int(rnum, 2)
