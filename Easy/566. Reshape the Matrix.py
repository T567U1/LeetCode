class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) == c:
            return nums
nums = [[1,2,3,4],[1,4,2,3]]
print(len(nums[0]))
