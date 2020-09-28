class Solution:
    def reverseBits(self, n: int) -> int:
        #zfill(uses whole byte)
        return int(str(bin(n)[2:].zfill(32)[::-1]), 2)
