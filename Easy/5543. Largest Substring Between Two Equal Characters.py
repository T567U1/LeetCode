class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        for i, y in enumerate(s):
            for j, x in enumerate(s[i + 1:]):
                if y == x:
                    ans = max(len(s[i:i + j]), ans)

        return ans
            
