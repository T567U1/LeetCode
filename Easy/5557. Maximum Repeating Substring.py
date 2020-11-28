class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        w = word
        while word in sequence:
            ans += 1
            word += w

        return ans
