class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count, ans = 0, 0
        for i in s:
            count += 1 if i == 'R' else -1
            ans += 1 if count == 0 else 0
        return ans
