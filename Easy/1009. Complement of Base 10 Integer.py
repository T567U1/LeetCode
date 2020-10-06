class Solution:
    def bitwiseComplement(self, N: int) -> int:
        rnum = ''
        for i in bin(N)[2:]:
            if i == '1':
                rnum += '0'
            else:
                rnum += '1'

        return int(rnum, 2)

#get the lenght substract 2 the b1 characters shift to left = 2 ^ len(c)
#and substract original number math hack....
#return (1<<(len(bin(N)) - 2)) - 1 - N
