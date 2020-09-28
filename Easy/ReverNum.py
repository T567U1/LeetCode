class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        p = str(x)
        r = str()
        for i in range(0, len(p)):
            print(r)
            if p[(len(p) -1) - i] == "-":
                r = '-' + r
                break
            r = r + str(int(p[(len(p) -1) - i]) % 10)
        return int(r)

p = Solution()
print(p.reverse(-254))
