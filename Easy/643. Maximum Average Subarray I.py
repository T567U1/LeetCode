class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        index, cur = k - 1, 0 # initialization
        cur = sum(nums[:k])
        res = cur
        while index + 1 < len(nums):
            index += 1  # move on
            cur = cur - nums[index - k] + nums[index]
            res = max(cur, res)
        return res / k
