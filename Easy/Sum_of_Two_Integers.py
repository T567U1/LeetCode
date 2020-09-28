class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        l = [a, b]
        return sum(l)

a = -2
b = 10
c = Solution()
print(c.getSum(a, b))
