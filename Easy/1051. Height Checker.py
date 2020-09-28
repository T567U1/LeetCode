class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        sorted_ = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != sorted_[i]:
                ans += 1

        return ans
