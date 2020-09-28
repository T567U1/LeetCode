class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        pows_of_three, pow = [1], 3
        while pow <= n:
            pows_of_three.append(pow)
            pow *= 3
        return n in pows_of_three

c = Solution()
print(c.isPowerOfThree(9))
