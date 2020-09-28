class Solution:
    def generateTheString(self, n: int) -> str:
        ans = ['a'] * n
        if n % 2 == 0:
            return ''.join(ans[:-1]) + 'b'
        return ''.join(ans)
