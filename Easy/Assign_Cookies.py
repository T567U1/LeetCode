class Solution:
    def findContentChildren(self, g, s) -> int:
        child, cookie_p, count, g, s = 0, 0, 0, sorted(g), sorted(s)

        while cookie_p < len(s) and child < len(g):
            print(cookie_p, child)
            if g[child] <= s[cookie_p]:
                count += 1
                child += 1
            cookie_p += 1

        return count
num, num1 = [], []
c = Solution()
print(c.findContentChildren(num, num1))
