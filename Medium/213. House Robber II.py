class Solution:
    def rob(self, nums: List[int]) -> int:
        def go(arr):
            x = y = 0
            for num in arr:
                x, y = y, max(x + num, y)
            return y

        return max(nums[0] + go(nums[2: -1]), go(nums[1:]))
