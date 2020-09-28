class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        for i in range(len(s)):
            if s[i] not in s[i + 1:] and s[i] not in s[:i]: return s.index(s[i])


c = Solution()
print(c.firstUniqChar('cc'))
