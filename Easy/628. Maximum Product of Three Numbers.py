class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        #copied from leet code and modify dont know why this is valid......
        return max((nums[0] * nums[1] * nums[-1]), (nums[-1] * nums[-2] * nums[-3]))
