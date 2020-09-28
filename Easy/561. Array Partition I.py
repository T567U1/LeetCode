class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        #nums = [min(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)]
        #return sum(nums)
        return sum(nums[::2])
