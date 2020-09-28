import math

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        zeros = 0
        while n > 5:
            n //= 5
            zeros += n

        return zeros

c = Solution()
print(c.trailingZeroes(9070))
