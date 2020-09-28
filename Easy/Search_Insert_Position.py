class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        for i, num in enumerate(nums):
            if num > target:
                return i
        return len(nums)


nums = [1,3,5,6]
cl = Solution()
print(cl.searchInsert(nums, 2))
