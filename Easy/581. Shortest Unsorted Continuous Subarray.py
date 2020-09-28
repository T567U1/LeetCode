class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if nums == sorted(nums):
            return 0
        start_index = []
        for i, (x, y) in enumerate(zip(nums, sorted(nums))):
            nums[i] = x - y
            if nums[i] != 0:
                start_index.append(i)
            
        return len(nums[start_index[0]:start_index[-1] + 1])
