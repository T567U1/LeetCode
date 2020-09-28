class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, 2)
        b = int(b, 2)
        r = bin(a + b)[2:]
        return r

c = Solution()
print(c.addBinary("1010", "1011"))
