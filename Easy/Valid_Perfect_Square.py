class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # take the square root of the number is used to get it mod as int
        num = num ** (1/2)
        return bool(num % int(num) == 0)

c = Solution()
print(c.isPerfectSquare(14))
