class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1: return True
        catch = []
        while n !=1:
            temp = 0
            while n > 0:
                temp += (n % 10) ** 2
                n = n//10
            n = temp
            if n == 1:
                return True
            elif n in catch:
                return False
            else:
                catch.append(temp)
c = Solution()
print(c.isHappy(2))
