class Solution:
    def findTheDifference(self, s: str, t: str):
        #just conver them to unico and minus the sums return chr()
        s = [ord(i) for i in s]
        t = [ord(i) for i in t]
        return chr(sum(t) - sum(s))

c = Solution()
print(c.findTheDifference("abcd", "abcde"))
