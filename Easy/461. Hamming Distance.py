class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(1 for a, b in zip(bin(x)[2:].zfill(32), bin(y)[2:].zfill(32)) if a != b)
