class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        rnum = ord(s[0]) - 64
        if len(s) > 1:
            rnum *= 26
            for i in range(1, len(s) - 1):
                rnum = (rnum + (ord(s[i]) - 64)) * 26
            rnum += ord(s[-1]) - 64
        return rnum
c = Solution()
print(c.titleToNumber("AA"))
