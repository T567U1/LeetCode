class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 0
        while n > i:
            i += 1
            n -= i

        return i

c = Solution()
print(c.arrangeCoins(10))
