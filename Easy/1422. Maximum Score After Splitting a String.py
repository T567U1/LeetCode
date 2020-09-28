class Solution:
    def maxScore(self, s: str) -> int:
        ans = []
        for i in range(1, len(s)):
            ans.append(s[i:].count('1') + s[:i].count('0'))
        return max(ans)
