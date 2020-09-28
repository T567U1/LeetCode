class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums_t = sorted(nums)
        if nums_t[-2] * 2 <= nums_t[-1]:
            return nums.index(nums_t[-1])
        return -1
