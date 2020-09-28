class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        s = s.split()
        while s:
            ans += s.pop() + " "
        return ans.strip()
