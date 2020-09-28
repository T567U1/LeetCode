class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0

c = Solution()
print(c.canWinNim(20))
