import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        Sieve of Eratosthenes
        from: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        """
        count = 0
        for num in range(n + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                    else:
                        count += 1
                        break

        return count
c = Solution()
print(c.countPrimes(100))
