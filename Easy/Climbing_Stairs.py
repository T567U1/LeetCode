class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return 1
        else:
            a, b = 1, 1
            for _ in range(2, n + 1):
                c = a + b
                a, b = b, c

            return c

c = Solution()
print(c.climbStairs(7))
