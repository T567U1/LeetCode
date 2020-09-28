class Solution:
    def countOdds(self, low: int, high: int) -> int:
        ans = (high - low) // 2
        add = 1 if high % 2 == 1 or low % 2 == 1 else 0
        return ans + add
