class Solution:
    def toHex(self, num: int) -> str:
        if num < 0: num += 2**32
        digits, sr = "0123456789abcdef", ''
        while num:
            sr += digits[num % 16]
            num //= 16
        return sr[::-1]

c =Solution()
print(c.toHex(-100000))
