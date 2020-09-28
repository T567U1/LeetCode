class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        dp = [1] * len(nums)
        for x in range(1, len(nums)):
            for y in range(x):
                if nums[y] < nums[x]:
                    dp[x] = max(dp[x], dp[y] + 1)

        return max(dp)
    
