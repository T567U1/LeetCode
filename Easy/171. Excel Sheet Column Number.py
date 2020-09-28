class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = [ (ord(i) + 1 - ord('A')) for i in s[:-1] ]
        ans = [ x * 26 ** len(ans[i:]) for i, x in enumerate(ans) ]
        return sum(ans) + (ord(s[-1]) + 1 - ord('A'))
