class Solution:
    def reverseWords(self, s: str) -> str:
        s = [i[::-1] for i in s.split()]
        s = " ".join(s)
        return s
