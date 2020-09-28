class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        s = list(s)

        while True:
            if not s or i >= len(s) - 1:
                return ''.join(s)
            if ord(s[i]) - 32 == ord(s[i + 1]) or ord(s[i]) + 32 == ord(s[i + 1]):
                s.pop(i + 1)
                s.pop(i)
                i = -1

            i += 1
