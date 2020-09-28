class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        m = nums[len(nums) // 2]
        count = 0
        for i in nums:
            count += abs(i - m)
        return count
