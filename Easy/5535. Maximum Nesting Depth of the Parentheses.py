class Solution:
    def maxDepth(self, s: str) -> int:
        ans = {}
        c = 0
        for i in s:
            if i == '(':
                c += 1
            elif i == ')':
                c -= 1
            if c in ans and i.isdigit():
                ans[c] = 1
            if c not in ans:
                    ans[c] = 0

        return max(ans)
