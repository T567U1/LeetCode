class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0: return 0
        #number is guaranty to be 9 or less
        return num % 9

c = Solution()
print(c.addDigits(38))
