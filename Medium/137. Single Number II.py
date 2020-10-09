class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums, key = lambda x: nums.count(x))
        return nums[0]
