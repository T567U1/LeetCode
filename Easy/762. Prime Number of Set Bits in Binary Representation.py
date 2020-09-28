class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        dic, count = {2:0, 3:0, 5:0, 7:0, 11:0, 13:0, 17:0, 19:0}, 0
        for i in range(L, R+1):
            if bin(i)[2:].count('1') in dic:
                count += 1

        return count
