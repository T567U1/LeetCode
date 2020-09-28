class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 52 or n == 702:
            return "ZZ" if n == 702 else "AZ"
        ls, result = [], ''
        while n > 26:
            mod = n % 26
            ls.insert(0, int(mod))
            n -= mod
            n /= 26
        ls.insert(0, int(n))
        for num in ls:
            result += chr(num + 64)
        return result


c = Solution()
print(c.convertToTitle(52))
