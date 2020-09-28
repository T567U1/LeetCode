class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s: return 1
        for i in s:
            if i not in t: return False
            t = t[t.index(i):]
        return True
c =Solution()
print(c.isSubsequence("acb", "ahbgdc"))
