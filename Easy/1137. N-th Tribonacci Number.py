class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1
        if n < 3:
            return 1 if n else 0
        ans = 0
        for i in range(3, n + 1):
            ans = a + b + c
            a, b, c = b, c, c + b + a

        return ans
