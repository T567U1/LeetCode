class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        nums = sorted(nums, key = lambda x: nums.count(x))
        return nums
