class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(set(nums)) == 1:
            return nums
        nums = sorted(nums, reverse = True)
        for i, x in enumerate(nums):
            if sum(nums[:i]) > sum(nums[i:]):
                return nums[:i]
