class Solution:
    def numSplits(self, s: str) -> int:
        x, y = collections.Counter(), collections.Counter(s)
        ans = 0
        for i in s[:-1]:
            x[i] += 1
            y[i] -= 1
            if not y[i]:
                del y[i]
            if len(x) == len(y):
                ans += 1

        return ans
