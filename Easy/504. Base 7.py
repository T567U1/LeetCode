class Solution:
    def convertToBase7(self, num: int) -> str:
        rs, minus_flag = "", 0
        if num < 0:
            minus_flag = 1
            num = abs(num)
        while num >= 7:
            rs += str(num % 7)
            num //= 7
        rs += str(num)
        if minus_flag: return '-' + rs[::-1]
        return rs[::-1]
