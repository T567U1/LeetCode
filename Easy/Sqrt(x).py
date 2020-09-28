import math

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = int(math.sqrt(x))
        return x

c = Solution()
print(c.mySqrt(4))
