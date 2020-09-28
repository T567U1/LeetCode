class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = 0
        ans = min(nums)
        for i in nums:
            a += i
            ans = max(a, ans)
            a = max(a, 0)
        return ans
