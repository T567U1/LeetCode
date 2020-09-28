class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #cheating????? it works so IDK
        if not num1 and not num2: return ''
        if not num1 or not num2: return num1 + num2
        return str(int(num1) + int(num2))

s, s1 = '10', '20'
c = Solution()
print(c.addStrings(s, s1))
