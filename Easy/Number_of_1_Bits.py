class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s1 = lambda x: format(x, 'b')
        s, list = s1(n), []
        for n in s:
            list.append(int(n))
        return sum(list)

n = 3
c = Solution()
print(c.hammingWeight(n))
