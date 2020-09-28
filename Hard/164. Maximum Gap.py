class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        ans = float("-inf")
        nums.sort()
        for i, x in enumerate(nums[:-1]):
            ans = max(ans, abs(nums[i + 1] - x))

        return ans
