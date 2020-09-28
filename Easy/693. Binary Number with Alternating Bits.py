class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return '00' not in bin(n)[2:] and '11' not in bin(n)[2:]
