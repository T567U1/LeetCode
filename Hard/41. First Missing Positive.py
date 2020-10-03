class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1 and nums[0] == 0:
            return 1
        m = min(nums)
        if m > 1:
            return 1
        nums.sort()
        while nums and nums[0] < 1:
            nums = nums[1:]

        i = 1
        while i in nums:
            i += 1

        return i
        
